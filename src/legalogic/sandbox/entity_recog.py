#! /usr/bin/env python3

"""
Recognize entities mentioned in the constitución.
"""

import argparse
import copy
import re
import sys
from typing import List

import pandas as pd
import spacy


def set_argparse() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Try sentence separation for constitucion_cr.txt .')
    parser.add_argument('-v', '--verbose', help='work verbosely', action="store_true")
    parser.add_argument('input_file_path', help='Path to the input file')

    args = parser.parse_args()
    args.prog = parser.prog

    return args


def proc_sent(nlp: spacy.Language, c_lines: List[str]):
    """Print entities recognized in the documents."""
    ent_list = []

    line = 0
    for line_text in c_lines:
        doc = nlp(line_text)
        for ent in doc.ents:
            ent_list.append({
                "text": ent.text,
                "line": line,
                "start": ent.start_char,
                "end": ent.end_char,
                "label": ent.label_,
                "kb_id": ent.kb_id,
            })
        line += 1

    df = pd.DataFrame(ent_list)
    print(df)


def main():
    args = set_argparse()

    input_file_path = args.input_file_path

    if args.verbose:
        print(f"Running {args.prog}:", file=sys.stderr)
        print(f"{input_file_path=}", file=sys.stderr)

    # read the file
    with open(input_file_path, encoding='utf-8') as c_file:
        c_lines = c_file.readlines()

    # using the dependency parse
    nlp = spacy.load("es_core_news_lg")

    proc_sent(nlp, c_lines[:5])


if __name__ == "__main__":
    main()
