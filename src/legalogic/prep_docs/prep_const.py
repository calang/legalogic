#! /usr/bin/env python3

import argparse
import copy
import re
import sys
from typing import List


# re flags to include new-lines
MULTI_FLAG = re.MULTILINE + re.DOTALL


def set_argparse() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Preprocess constitucion_cr-26.html file.')
    parser.add_argument('-v', '--verbose', help='work verbosely', action="store_true")
    parser.add_argument('input_file_path', help='Path to the input file')

    args = parser.parse_args()
    args.prog = parser.prog

    return args


def clean_text(in_txt: str) -> str:
    """Remove all undesired text from the input"""
    c_text = copy.copy(in_txt)

    # pattern for html comments
    comment_pattern = re.compile(pattern=r'<!--.*-->', flags=MULTI_FLAG)

    # pattern for any other html tag
    tag_pattern = re.compile(pattern=r'<[^>]*>', flags=MULTI_FLAG)


    # patterns for instances of &nbsp;
    nbsp_html_pattern = re.compile(pattern=r'&nbsp;', flags=MULTI_FLAG)
    nbsp_pattern = re.compile(pattern='\u00A0', flags=MULTI_FLAG)

    # patter for Ficha articulo
    ficha_pattern = re.compile(pattern=r'\s*Ficha articulo\s*')

    c_text = re.sub(comment_pattern, '', c_text)
    c_text = re.sub(tag_pattern, '', c_text)
    c_text = re.sub(nbsp_html_pattern, ' ', c_text)
    c_text = re.sub(nbsp_pattern, ' ', c_text)
    c_text = re.sub(ficha_pattern, '', c_text)

    # assert c_text is not in_txt, "c_text and in_text are the same"
    return c_text


def get_article_list(in_text: str) -> List[str]:
    """
    Extract article text,
    including all their paragraphs,
    including parenthesized comments.
    """
    # remove all nl
    article_text = in_text.replace('\n', ' ')

    # split text by 'ARTÍCULO', removing first item
    article_list = re.split('ARTÍCULO', article_text, flags=MULTI_FLAG)[1:]

    # replace "ARTÍCULO" in front of each article
    article_list = list(map(lambda x: "ARTÍCULO" + x, article_list))

    # remove any left-over "TITULO ..." from the item text
    article_list = list(map(lambda x: x.split("TITULO")[0], article_list))

    return article_list


def main():
    args = set_argparse()
    input_file_path = args.input_file_path

    if args.verbose:
        print(f"Running {args.prog}:", file=sys.stderr)
        print(f"{input_file_path=}", file=sys.stderr)

    # read the file
    with open(input_file_path, encoding='windows-1252') as c_file:
        c_text = c_file.read()

    # confirm default output encoding
    sys.stdout.reconfigure(encoding='utf-8')

    simplified_text = clean_text(c_text)
    article_list = get_article_list(simplified_text)

    for art in article_list:
        print(art)


if __name__ == "__main__":
    main()
