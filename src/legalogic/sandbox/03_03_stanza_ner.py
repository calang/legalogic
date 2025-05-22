#!/usr/bin/env python
"""
Obtain a list of identified Named Entities from constitución text.
"""

import argparse

import stanza

from src.util.pandas_config import configure_pandas_display

configure_pandas_display()


def set_argparse() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Obtain a list of identified Named Entities from constitución text.')
    parser.add_argument('-v', '--verbose',
                        help='work verbosely',
                        action="store_true"
                        )
    parser.add_argument('-m', '--maxlines',
                        type=int,
                        help='max number of input lines to process',
                        )
    parser.add_argument('input_file_path',
                        help='Path to the input file'
                        )
    args = parser.parse_args()
    args.prog = parser.prog
    return args


def init_nlp(use_gpu: bool = True) -> stanza.Pipeline:
    """
    Initialize the Stanza NLP pipeline.
    
    Args:
        use_gpu: Whether to use GPU acceleration if available
    
    Returns:
        Stanza Pipeline object or None if initialization fails
    
    Raises:
        stanza.pipeline.core.ResourcesFileNotFoundError: If required models are not downloaded
        RuntimeError: If pipeline initialization fails
    """
    try:
        return stanza.Pipeline('es',
                               use_gpu=use_gpu,
                               processors='tokenize,mwt,ner',
                               download_method=None,
                               )
    except stanza.pipeline.core.ResourcesFileNotFoundError as e:
        print(f"Required Stanza models not found. Please download models first: {e}")
        return None
    except RuntimeError as e:
        print(f"Failed to initialize Stanza pipeline: {e}")
        return None


def process_file(file_path: str, nlp: stanza.Pipeline, maxlines: int = None) -> None:
    """
    Process a text file.
    
    Args:
        file_path: Path to the input file
        nlp: Initialized Stanza pipeline
        maxlines: Maximum number of lines to process from input file
    
    Raises:
        FileNotFoundError: If input file does not exist
        Exception: If dependency parsing fails
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            line_text_list = f.readlines()

        for line_text in line_text_list[:(maxlines if maxlines else 1000000)]:
            doc = nlp(line_text)
            print(f"\n{doc.text}")
            for ent in doc.ents:
                print(f'entity: {ent.text}\t: {ent.type}')
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
    except Exception as e:
        print(f"Error processing file: {e}")


def main():
    args = set_argparse()
    nlp = init_nlp()
    if nlp is None:
        return
    
    process_file(args.input_file_path, nlp, args.maxlines)


if __name__ == '__main__':
    main()