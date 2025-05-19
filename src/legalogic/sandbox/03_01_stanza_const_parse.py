#!/usr/bin/env python
"""
Obtain Constituency Grammar Trees from constitución text.
This script processes Spanish text and generates constituency grammar trees using Stanza.
"""

import argparse
import stanza


def set_argparse() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Obtain Constituency Grammar Trees from constitución text.')
    parser.add_argument('-v', '--verbose', help='work verbosely', action="store_true")
    parser.add_argument('input_file_path', help='Path to the input file')
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
        return stanza.Pipeline('es', use_gpu=use_gpu, processors='tokenize,pos,constituency')
    except Exception as e:
        print(f"Failed to initialize Stanza pipeline: {e}")
        return None


def process_file(file_path: str, nlp: stanza.Pipeline) -> None:
    """
    Process a text file and print its constituency trees.
    
    Args:
        file_path: Path to the input file
        nlp: Initialized Stanza pipeline
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        doc = nlp(text)
        for sentence in doc.sentences[:5]:
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
    
    process_file(args.input_file_path, nlp)


if __name__ == '__main__':
    main()