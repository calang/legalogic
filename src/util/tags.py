#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Universal Dependencies tag dictionaries.

Ref: https://universaldependencies.org/u/pos/
"""

"""
POS tags from Universal Dependencies.
"""
upos_tags = {
    'ADJ': 'adjective',
    'ADP': 'adposition',
    'ADV': 'adverb',
    'AUX': 'auxiliary',
    'CCONJ': 'coordinating conjunction',
    'DET': 'determiner',
    'INTJ': 'interjection',
    'NOUN': 'noun',
    'NUM': 'numeral',
    'PART': 'particle',
    'PRON': 'pronoun',
    'PROPN': 'proper noun',
    'PUNCT': 'punctuation',
    'SCONJ': 'subordinating conjunction',
    'SYM': 'symbol',
    'VERB': 'verb',
    'X': 'other',
}

"""
Grammatical categories that show up in the constituency parse tree.
"""
gram_categories = {
    'ROOT',
    'S',
    'conj',
    'gerundi',
    'grup.a',
    'grup.adv',
    'grup.cc',
    'grup.cs',
    'grup.nom',
    'grup.prep',
    'grup.pron',
    'grup.verb',
    'grup.w',
    'grup.z',
    'inc',
    'infinitiu',
    'interjeccio',
    'morfema.pronominal',
    'morfema.verbal',
    'neg',
    'participi',
    'prep',
    'relatiu',
    's.a',
    'sadv',
    'sentence',
    'sn',
    'sp',
    'spec',
}
