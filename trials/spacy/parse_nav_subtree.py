import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Credit and mortgage account holders must submit their requests")

root = [token for token in doc if token.head == token][0]
print(root.text, root.dep_, root.n_lefts, root.n_rights)

subject = list(root.lefts)[0]
print(subject.text, subject.dep_, subject.n_lefts, subject.n_rights)

for descendant in subject.subtree:
    assert subject is descendant or subject.is_ancestor(descendant)
    print(descendant.text, descendant.dep_, descendant.n_lefts,
            descendant.n_rights,
            [ancestor.text for ancestor in descendant.ancestors])

with open('sub_tree.svg', 'w') as f:
    f.write(displacy.render(doc, style="dep"))
