#!/usr/bin/env python
"""
Obtain a list of co-referenced Named Entities from constitución text.
"""

import argparse
import pprint as pp

import stanza

from src.config.config import Config
from src.util.pandas_config import configure_pandas_display

config = Config().config
configure_pandas_display()


def set_argparse() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Obtain a list of co-referenced Named Entities from constitución text.')
    parser.add_argument('-v', '--verbose',
                        help='work verbosely',
                        action="store_true"
                        )
    parser.add_argument('-m', '--maxlines',
                        type=int,
                        help='max number of input lines to process',
                        )
    parser.add_argument('-s', '--summarize',
                        help='print a set of coref representative texts for each document',
                        action="store_true",
                        )
    parser.add_argument('input_file_path',
                        help='Path to the input file'
                        )
    args = parser.parse_args()
    args.prog = parser.prog
    return args


def init_nlp(use_gpu: bool = False) -> stanza.Pipeline:
    """
    Initialize the Stanza NLP pipeline.
    
    Args:
        use_gpu: Whether to use GPU acceleration if available
    
    Returns:
        Stanza Pipeline object or None if initialization fails
    
    Raises:
        Exception: If pipeline initialization fails
    """
    try:
        return stanza.Pipeline('es',
                               use_gpu=use_gpu,
                               processors='tokenize,mwt,coref',
                               download_method=None,  # to save queries to source
                               )
    except Exception as e:
        raise Exception(f"Failed to initialize Stanza pipeline: {e}") from e


def process_file(file_path: str,
                 nlp: stanza.Pipeline,
                 maxlines: int = None,
                 summarize: bool = False,
                 ) -> None:
    """
    Process a text file for co-reference analysis.
    
    Args:
        file_path: Path to the input file to process
        nlp: Initialized Stanza pipeline for text processing
        maxlines: Maximum number of lines to process from input file (None for all lines)
        summarize: If True, print a set of co-reference representative texts for each document
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        line_text_list = f.readlines()

    for line_text in line_text_list[:maxlines if maxlines else config.get('maxlines_infinite')]:
        print(f"\n{line_text}")
        doc = nlp(line_text)
        print(f"{doc:C}")
        if summarize:
            print('Coref representative texts:')
            coref_text_set = set()
            for word in doc.iter_words():
                for coref_att in word.coref_chains:
                    coref_text_set.add(coref_att.chain.representative_text)
            pp.pprint(coref_text_set)
        print()


def main():
    args = set_argparse()
    nlp = init_nlp()
    if nlp is None:
        return

    process_file(args.input_file_path, nlp, args.maxlines, args.summarize)


if __name__ == '__main__':
    main()