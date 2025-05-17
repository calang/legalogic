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
from spacy import displacy
from spacy.tokens import Span, Token


def set_argparse() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Try sentence separation for constitucion_cr.txt .')
    parser.add_argument('-v', '--verbose', help='work verbosely', action="store_true")
    parser.add_argument('input_file_path', help='Path to the input file')

    args = parser.parse_args()
    args.prog = parser.prog

    return args


def print_entities(nlp: spacy.Language, c_lines: List[str]):
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


def print_token_parse_tree(node: Token, indent: int = 0):
    ADD_INDENT = 4

    print(f"{indent * ' '}[{node.i}] {node.text}\t\t"
          f" dep_: {node.dep_}, "
          f" pos_: {node.pos_}, "
          f" tag_: {node.tag_}, "
          f" iob_: {node.ent_iob_}"
          )

    for c in node.children:
        print_token_parse_tree(c, indent + ADD_INDENT)


def print_sent_parse_tree(sent: Span):
    root = sent.root
    print_token_parse_tree(root)


def print_parse_trees(nlp: spacy.Language, c_lines: List[str]):
    """Print parse trees for each of the line documents."""
    line = 0
    for line_text in c_lines:
        doc = nlp(line_text)
        for sent in doc.sents:
            print(f"\nSentence [{line}]: {sent.text}")
            print_sent_parse_tree(sent)
        line += 1


def render_parse_trees(nlp: spacy.Language, c_lines: List[str], out_file: str):
    """Create displaCy html file with each of the line documents parse trees."""
    docs = [nlp(line) for line in c_lines]

    html = displacy.render(docs)

    with open(out_file, "w", encoding='utf-8') as outf:
        outf.write(html)


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

    print_entities(nlp, c_lines[:5])

    print_parse_trees(nlp, c_lines[:5])

    render_parse_trees(nlp, c_lines[:5], 'src/legalogic/sandbox/01-const_trees.html')


if __name__ == "__main__":
    main()
