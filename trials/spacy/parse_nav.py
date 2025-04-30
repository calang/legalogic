import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("bright red apples on the tree")
print([token.text for token in doc[2].lefts])  # ['bright', 'red']
print([token.text for token in doc[2].rights])  # ['on']
print(doc[2].n_lefts)  # 2
print(doc[2].n_rights)  # 1

print([token.text for token in doc[3].lefts])  # ['bright', 'red']
print([token.text for token in doc[3].rights])  # ['on']
print(doc[3].n_lefts)  # 2
print(doc[3].n_rights)  # 1

with open('tree.svg', 'w') as f:
    f.write(displacy.render(doc, style="dep"))
