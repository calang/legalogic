#!/usr/bin/env python
"""
Obtain Constituency Grammar Trees from constitución text.
This script processes Spanish text and generates constituency grammar trees using Stanza.
"""

import argparse
from collections import Counter
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
    parser.add_argument('-g', '--grupnom',
                        help='collapse each grup.nom as a single leaf node',
                        action="store_true",
                        )
    parser.add_argument('-c', '--categories',
                        help='produce a set of gramatical categories at the end of the output',
                        action="store_true",
                        )
    parser.add_argument('-t', '--treenodes',
                        help='produce a Counter of tree nodes at the end of the output',
                        action="store_true",
                        )
    parser.add_argument('-s', '--summarize',
                        help='summarize accumulated counts for each line (default: False)',
                        action="store_true",
                        )
    parser.add_argument('input_file_path',
                        help='Path to the input file'
                        )
    args = parser.parse_args()
    args.prog = parser.prog
    
    args.grupnom = args.grupnom or args.summarize
    
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
               grupnom: bool = False,
               summarize: bool = False,
               categories: bool = False,
               treenodes: bool = False,
               ) -> set[str]:
    """
    Print a constituency parse tree with proper indentation.
    
    Args:
        tree: The constituency parse tree object to print
        indent: Number of spaces for indentation (default: 0)
        grupnom: Whether to collapse grup.noms as single leaf nodes (default: False)
        summarize: Whether to summarize accumulated counts for each line (default: False)
        categories: Whether to produce a set of gramatical categories at the end of the output (default: False)
        treenodes: Whether to produce a Counter of tree nodes at the end of the output (default: False)
    
    Returns:
        - set of collapsed grup.noms if summarize is True, else the empty set
        - set of gramatical categories if categories is True, else the empty set
        - Counter of tree nodes if treenodes is True, else the empty set
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

    treenode_count = Counter()
    if treenodes and tree.label not in upos_tags and tree.children:
        new_node = (tree.label, ) + tuple(c.label for c in tree.children)
        treenode_count[new_node] += 1

    if grupnom and tree.label == 'grup.nom':
        group_text = get_tree_text(tree)
        print(f"{' ' * indent}{tree.label} {group_text}")
        return ({group_text} if summarize else set(),
                category_set,
                treenode_count,
                )

    if tree.label in upos_tags:
        print(f"{' ' * indent}{tree.label} {tree.children[0].label}")
        return set(), category_set, treenode_count

    print(f"{' ' * indent}{tree.label}")
    grupnom_set = set()
    for child in tree.children:
        grupnom_subset, category_subset, treenode_subcount = (
            print_tree(child,
                       indent + INDENT_SIZE,
                       grupnom=grupnom,
                       summarize=summarize,
                       categories=categories,
                       treenodes=treenodes,
                       )
        )
        grupnom_set |= grupnom_subset
        category_set |= category_subset
        treenode_count += treenode_subcount
    return grupnom_set, category_set, treenode_count


def process_file(file_path: str,
                 nlp: stanza.Pipeline,
                 maxlines: int = None,
                 grupnom: bool = False,
                 summarize: bool = False,
                 categories: bool = False,
                 treenodes: bool = False,
                 ) -> None:
    """
    Process a text file and print its constituency trees.
    
    Args:
        file_path: Path to the input file
        nlp: Initialized Stanza pipeline
        maxlines: Maximum number of lines to process from input file
        grupnom: Whether to collapse grup.noms as single leaf nodes (default: False)
        summarize: Whether to summarize accumulated counts for each line (default: False)
        categories: Whether to produce a set of gramatical categories at the end of the output (default: False)
        treenodes: Whether to produce a Counter of tree nodes at the end of the output (default: False)

    Raises:
        FileNotFoundError: If input file does not exist
        Exception: If parsing fails
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            line_text_list = f.readlines()

        all_category_set = set()
        all_treenode_counts = Counter()
        for line_text in line_text_list[:maxlines]:
            doc = nlp(line_text)
            for sentence in doc.sentences:
                print(sentence.text)
                tree = sentence.constituency
                print(tree)
                grupnom_set, category_set, treenode_count = print_tree(tree,
                                                                        grupnom=grupnom,
                                                                        summarize=summarize,
                                                                        categories=categories,
                                                                        treenodes=treenodes,
                                                                        )
                if summarize:
                    if grupnom:
                        print('Set of grup.nom:')
                        pp.pprint(grupnom_set)
                    if categories:
                        print(f'Set of gramatical categories ({len(category_set)}):')
                        pp.pprint(category_set)
                    if treenodes:
                        print(f'Tree nodes count: ({len(treenode_count)}):')
                        pp.pprint(treenode_count)
                if categories:
                    all_category_set |= category_set
                if treenodes:
                    all_treenode_counts += treenode_count
                print()
        print(f'Total different gramatical categories ({len(all_category_set)}):')
        pp.pprint(all_category_set)
        print(f'Total tree node counts: ({len(all_treenode_counts)}):')
        pp.pprint(all_treenode_counts)
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
                 args.grupnom,
                 args.summarize,
                 args.categories,
                 args.treenodes,
                 )


if __name__ == '__main__':
    main()