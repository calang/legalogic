#! /usr/bin/env python3

import argparse
import re
import sys


def set_argparse() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Preprocess constitucion_cr.html file.')
    parser.add_argument('-v', '--verbose', help='work verbosely', action="store_true")
    parser.add_argument('input_file_path', help='Path to the input file')

    args = parser.parse_args()
    args.prog = parser.prog

    return args


def main():
    args = set_argparse()
    input_file_path = args.input_file_path

    if args.verbose:
        print(f"Running {args.prog}:", file=sys.stderr)
        print(f"{input_file_path=}", file=sys.stderr)

    # read the file
    with open(input_file_path, encoding='windows-1252') as c_file:
        c_text = c_file.read()

    # pattern to remove html comments
    comment_pattern = re.compile(pattern=r'<!--.*-->',
                                 flags=re.MULTILINE + re.DOTALL
                                 )
    # pattern to remove any other html tag
    tag_pattern = re.compile(pattern=r'<[^>]*>',
                             flags=re.MULTILINE + re.DOTALL
                             )

    # pattern to remove instances of &nbsp;
    nbsp_pattern = re.compile(pattern=r'&nbsp;',
                              flags=re.MULTILINE + re.DOTALL
                              )

    c_text = re.sub(comment_pattern, '', c_text)
    c_text = re.sub(tag_pattern, '', c_text)
    c_text = re.sub(nbsp_pattern, '', c_text)

    # confirm default output encoding
    sys.stdout.reconfigure(encoding='utf-8')

    print(c_text)


if __name__ == "__main__":
    main()
