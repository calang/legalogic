#!/usr/bin/env python
"""
Obtain Constituency Grammar Trees from constitución text.
This script processes Spanish text and generates constituency grammar trees using Stanza.
"""

import argparse
import stanza
from src.util.tags import upos_tags


def set_argparse() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Obtain Constituency Grammar Trees from constitución text.')
    parser.add_argument('-v', '--verbose',
                        help='work verbosely',
                        action="store_true",
                        )
    parser.add_argument('-m', '--maxlines',
                        type=int,
                        help='max number of input lines to process',
                        )
    parser.add_argument('-g', '--groupnom',
                        help='collapse group names as a single leaf node',
                        action="store_true",
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
        Exception: If pipeline initialization fails for any reason
    """
    try:
        return stanza.Pipeline('es',
                               use_gpu=use_gpu,
                               processors='tokenize,mwt,pos,constituency',
                               download_method=None,
                               )
    except Exception as e:
        raise Exception(f"Failed to initialize Stanza pipeline: {e}") from e


def print_tree(tree: 'ParseTree', indent: int = 0, group_nom: bool = False) -> None:
    """
    Print a constituency parse tree with proper indentation.
    
    Args:
        tree: The constituency parse tree object to print
        indent: Number of spaces for indentation (default: 0)
        group_nom: Whether to collapse group names as single leaf nodes (default: False)
    """
    INDENT_SIZE = 4  # Number of spaces for each level of indentation

    def get_tree_text(tree: 'ParseTree') -> str:
        """Return text for the whole tree, with a prefix."""

        if not tree.children:
            return tree.label

        return ' '.join([get_tree_text(c) for c in tree.children])

    if group_nom and tree.label == 'grup.nom':
        group_text = get_tree_text(tree)
        print(f"{' ' * indent}{tree.label} {group_text}")
        return

    if tree.label in upos_tags:
        print(f"{' ' * indent}{tree.label} {tree.children[0].label}")
        return

    print(f"{' ' * indent}{tree.label}")
    for child in tree.children:
        print_tree(child, indent + INDENT_SIZE, group_nom=group_nom)


def process_file(file_path: str,
                 nlp: stanza.Pipeline,
                 maxlines: int = None,
                 group_nom: bool = False,
                 ) -> None:
    """
    Process a text file and print its constituency trees.
    
    Args:
        file_path: Path to the input file
        nlp: Initialized Stanza pipeline
        maxlines: Maximum number of lines to process from input file
        group_nom: Whether to collapse group names as single leaf nodes (default: False)

    Raises:
        FileNotFoundError: If input file does not exist
        Exception: If parsing fails
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            line_text_list = f.readlines()
        for line_text in line_text_list[:maxlines]:
            doc = nlp(line_text)
            for sentence in doc.sentences:
                print(sentence.text)
                tree = sentence.constituency
                print_tree(tree, group_nom=group_nom)
                print()
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
    except Exception as e:
        print(f"Error processing file: {e}")


def main():
    args = set_argparse()
    nlp = init_nlp()
    if nlp is None:
        return

    process_file(args.input_file_path, nlp, args.maxlines, args.groupnom)


if __name__ == '__main__':
    main()