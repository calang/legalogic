import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

for token in doc:
    print('\t'.join([token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            token.shape_, str(token.is_alpha), str(token.is_stop)]))

# displacy.serve(doc, style="dep")
# displacy.render(doc, style="dep")
