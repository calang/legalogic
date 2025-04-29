# test spacy GPU enablement

import pprint as pp
import spacy

print(f"GPU active: {spacy.require_gpu()}")
nlp = spacy.load("en_core_web_sm")
pp.pprint(spacy.info())
