#! /usr/bin/env python

import spacy
import benepar
import nltk

# Load Spanish spaCy model
nlp = spacy.load("es_core_news_md")

# produces an error: benepar_es3 is not available
benepar.download("benepar_es3")

# Add Benepar component to the pipeline
nlp.add_pipe("benepar", config={"model": "benepar_es3"})

# Process Spanish text
text = "El gato duerme en el sofá. La comida está preparada."
doc = nlp(text)

# Extract constituency parses
for sent in doc.sents:
    print(f"Sentence: {sent.text}")
    print(f"Parse tree: {sent._.parse_string}\n")
