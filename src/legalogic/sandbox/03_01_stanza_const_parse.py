#!/usr/bin/env python
"""
Obtain Constituency Grammar Trees from constitución text.
This script processes Spanish text and generates constituency grammar trees using Stanza.
"""

import argparse
import pprint as pp

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
    parser.add_argument('-c', '--categories',
                        help='produce a list of group categories at the end of the output',
                        action="store_true",
                        )
    parser.add_argument('-s', '--summarize',
                        help='include a list of collapsed grupnoms for each sentence; implies -g if not already set',
                        action="store_true",
                        )
    parser.add_argument('input_file_path',
                        help='Path to the input file'
                        )
    args = parser.parse_args()
    args.prog = parser.prog
    
    args.groupnom = args.groupnom or args.summarize
    
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


def print_tree(tree: 'ParseTree',
               indent: int = 0,
               group_nom: bool = False,
               summarize: bool = False,
               categories: bool = False,
               ) -> set[str]:
    """
    Print a constituency parse tree with proper indentation.
    
    Args:
        tree: The constituency parse tree object to print
        indent: Number of spaces for indentation (default: 0)
        group_nom: Whether to collapse group names as single leaf nodes (default: False)
        summarize: Whether to produce a list of collapsed group names for each sentence (default: False)
        categories: Whether to produce a list of group categories at the end of the output (default: False)
    
    Returns:
        - set of collapsed group names if summarize is True, else the empty set
        - set of group categories if categories is True, else the empty set
    """
    INDENT_SIZE = 4  # Number of spaces for each level of indentation

    def get_tree_text(tree: 'ParseTree') -> str:
        """Return text for the whole tree."""

        if not tree.children:
            return tree.label

        return ' '.join([get_tree_text(c) for c in tree.children])

    category_set = set()
    if categories and tree.label not in upos_tags:
        category_set.add(tree.label)

    if group_nom and tree.label == 'grup.nom':
        group_text = get_tree_text(tree)
        print(f"{' ' * indent}{tree.label} {group_text}")
        return ({group_text} if summarize else set(),
                category_set
                )

    if tree.label in upos_tags:
        print(f"{' ' * indent}{tree.label} {tree.children[0].label}")
        return set(), category_set

    print(f"{' ' * indent}{tree.label}")
    group_nom_set = set()
    for child in tree.children:
        group_nom_subset, category_subset = print_tree(child,
                                                       indent + INDENT_SIZE,
                                                       group_nom=group_nom,
                                                       summarize=summarize,
                                                       categories=categories,
                                                       )
        group_nom_set |= group_nom_subset
        category_set |= category_subset
    return group_nom_set, category_set


def process_file(file_path: str,
                 nlp: stanza.Pipeline,
                 maxlines: int = None,
                 group_nom: bool = False,
                 summarize: bool = False,
                 categories: bool = False,
                 ) -> None:
    """
    Process a text file and print its constituency trees.
    
    Args:
        file_path: Path to the input file
        nlp: Initialized Stanza pipeline
        maxlines: Maximum number of lines to process from input file
        group_nom: Whether to collapse group names as single leaf nodes (default: False)
        summarize: Whether to include a list of collapsed group names for each sentence (default: False)
        categories: Whether to produce a list of group categories at the end of the output (default: False)

    Raises:
        FileNotFoundError: If input file does not exist
        Exception: If parsing fails
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            line_text_list = f.readlines()

        all_category_set = set()
        for line_text in line_text_list[:maxlines]:
            doc = nlp(line_text)
            for sentence in doc.sentences:
                print(sentence.text)
                tree = sentence.constituency
                print(tree)
                group_name_set, category_set = print_tree(tree, group_nom=group_nom, summarize=summarize, categories=categories)
                if summarize:
                    print('Group names:')
                    pp.pprint(group_name_set)
                if categories:
                    all_category_set |= category_set
                print()
        print('Group categories:')
        pp.pprint(all_category_set)
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
    except Exception as e:
        print(f"Error processing file: {e}")


def main():
    args = set_argparse()
    nlp = init_nlp()
    if nlp is None:
        return

    process_file(args.input_file_path,
                 nlp,
                 args.maxlines,
                 args.groupnom,
                 args.summarize,
                 args.categories,
                 )


if __name__ == '__main__':
    main()