#!/usr/bin/env python
"""
Obtain a Dependency Parse from constitución text.
"""

import argparse
from collections import Counter
import pprint as pp
import sys

import numpy as np
import pandas as pd
import stanza

from src.util.pandas_config import configure_pandas_display

configure_pandas_display()


def set_argparse() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Obtain a Dependency Parse from constitución text.')
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
        Exception: If pipeline initialization fails
    """
    try:
        return stanza.Pipeline('es',
                               use_gpu=use_gpu,
                               processors='tokenize,mwt,pos,lemma,depparse',
                               download_method=None,
                               )
    except Exception as e:
        raise Exception(f"Failed to initialize Stanza pipeline: {e}") from e


def print_deptree(df: pd.DataFrame, node_index: np.int64, indent: int = 0) -> None:
    """
    Recursively print dependency tree structure.
    
    Args:
        df: DataFrame containing parsed sentence information
        node_index: Index of the current node in the DataFrame
        indent: Number of spaces for indentation level
    """
    INDENT_SIZE = 4

    print(f"{" " * indent}{df.loc[node_index, "word"]} -- {df.loc[node_index, "deprel"]}")

    idx = df.loc[node_index, "id"]
    children_indexes = df[df['head_id'] == idx].index

    for child_ix in children_indexes:
        print_deptree(df, child_ix, indent + INDENT_SIZE)


def process_file(file_path: str, nlp: stanza.Pipeline, maxlines: int = None) -> None:
    """
    Process a text file and print its dependency trees.
    
    Args:
        file_path: Path to the input file
        nlp: Initialized Stanza pipeline
        maxlines: Maximum number of lines to process from input file
    
    Raises:
        FileNotFoundError: If input file does not exist
        ValueError: If dependency parsing fails
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            line_text_list = f.readlines()

        total_pos_counts = Counter()
        total_deprel_pos_counts = Counter()
        total_deprel_pos_lemma_counts = Counter()

        for line_text in line_text_list[:(maxlines if maxlines else 1000000)]:
            doc = nlp(line_text)
            for sent in doc.sentences:
                print(f"\n{sent.text}")
                dep_list = []
                for word in sent.words:
                    dep_dict = {
                        'id': word.id,
                        'word': word.text,
                        'head_id': word.head,
                        'head': sent.words[word.head - 1].text if word.head > 0 else "root",
                        'deprel': word.deprel,
                        'pos': word.upos,
                        'lemma': word.lemma,
                        'feats': word.feats,
                        'misc': word.misc
                    }
                    total_pos_counts[word.upos] += 1
                    total_deprel_pos_counts[(word.deprel,word.pos)] += 1
                    total_deprel_pos_lemma_counts[(word.deprel,word.pos,word.lemma)] += 1
                    dep_list.append(dep_dict)
                df = pd.DataFrame(dep_list)
                print(df)
                try:
                    root_index = df[df['head'] == "root"].index[0]
                except Exception as e:
                    raise Exception(f"Exception while looking for head == root: {e}") from e
                print_deptree(df, root_index)
        pp.pprint(f"\nTotal POS counts: {total_pos_counts}")
        pp.pprint(f"\nTotal DEPREL-POS counts: {total_deprel_pos_counts}")
        pp.pprint(f"\nTotal DEPREL-POS-LEMMA counts: {total_deprel_pos_lemma_counts}")
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