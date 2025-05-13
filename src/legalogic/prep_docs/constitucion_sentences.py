#! /usr/bin/env python3

"""
Read separate sentences from constitucion_cr.txt
"""

import argparse
import copy
import re
import sys
import time
from typing import List

import spacy


def set_argparse() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Try sentence separation for constitucion_cr.txt .')
    parser.add_argument('-v', '--verbose', help='work verbosely', action="store_true")
    parser.add_argument('input_file_path', help='Path to the input file')

    args = parser.parse_args()
    args.prog = parser.prog

    return args


def remove_art_num_prefix(in_txt: str) -> str:
    """Remove article number prefix"""
    c_text = copy.copy(in_txt)

    # pattern for article number prefix
    art_pattern = re.compile(r'^ARTÍCULO [0-9]+º?.-?\s*(.-)?')

    c_text = re.sub(art_pattern, '', c_text)

    # assert c_text is not in_txt, "c_text and in_text are the same"
    return c_text


def proc_sent(nlp: spacy.Language, c_lines: List[str]):
    """Print lines without initial or ending space in any of its sentences."""
    for line_text in c_lines:
        doc = nlp(line_text)
        sent_list = [sent.text.strip() for sent in doc.sents]
        print(''.join(sent_list))


def main():
    args = set_argparse()

    input_file_path = args.input_file_path

    if args.verbose:
        print(f"Running {args.prog}:", file=sys.stderr)
        print(f"{input_file_path=}", file=sys.stderr)

    # read the file
    with open(input_file_path, encoding='utf-8') as c_file:
        c_lines = [
            remove_art_num_prefix(line)
            for line in c_file
        ]

    # using the dependency parse
    nlp = spacy.load("en_core_web_sm")

    proc_sent(nlp, c_lines)


if __name__ == "__main__":
    main()
