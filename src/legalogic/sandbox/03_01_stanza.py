#!/usr/bin/env python

import stanza
import torch

print(f"{torch.cuda.is_available()=}")  # Should return True

nlp = stanza.Pipeline('es', use_gpu=True)

def print_tree(tree, indent: int = 0):
    ADD_INDENT = 4

    print(f"{indent * ' '}{tree.label}")
    for child in tree.children:
        print_tree(child, indent + ADD_INDENT)

# text = """Costa Rica es una República"""

text = """Costa Rica es una República democrática, libre, independiente, multiétnica y pluricultural.
(Así reformado por el artículo único de la Ley N° 9305 del 24 de agosto del 2015)"""

doc = nlp(text)

for sentence in doc.sentences:
    tree = sentence.constituency
    print(tree)
    print_tree(tree)

