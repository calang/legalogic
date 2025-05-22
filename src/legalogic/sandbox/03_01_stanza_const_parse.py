#!/usr/bin/env python
"""
Obtain Constituency Grammar Trees from constitución text.
This script processes Spanish text and generates constituency grammar trees using Stanza.
"""

import argparse
import stanza


def set_argparse() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Obtain Constituency Grammar Trees from constitución text.')
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


def print_tree(tree: 'ParseTree', indent: int = 0) -> None:
    """
    Print a constituency parse tree with proper indentation.
    
    Args:
        tree: The constituency parse tree object to print
        indent: Number of spaces for indentation (default: 0)
    """
    INDENT_SIZE = 4  # Number of spaces for each level of indentation
    print(f"{' ' * indent}{tree.label}")
    for child in tree.children:
        print_tree(child, indent + INDENT_SIZE)


def init_nlp(use_gpu: bool = True) -> stanza.Pipeline:
    """
    Initialize the Stanza NLP pipeline.
    
    Args:
        use_gpu: Whether to use GPU acceleration if available
    
    Returns:
        Stanza Pipeline object or None if initialization fails
    """
    try:
        return stanza.Pipeline('es',
                               use_gpu=use_gpu,
                               processors='tokenize,pos,constituency',
                               download_method=None,
                               )
    except Exception as e:
        print(f"Failed to initialize Stanza pipeline: {e}")
        return None


def process_file(file_path: str, nlp: stanza.Pipeline, maxlines: int = None) -> None:
    """
    Process a text file and print its constituency trees.
    
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
        for line_text in line_text_list[:5]:
            doc = nlp(line_text)
            for sentence in doc.sentences:
                print(sentence.text)
                tree = sentence.constituency
                print_tree(tree)
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