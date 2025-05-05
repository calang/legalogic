import spacy
from spacy.language import Language

@Language.component("custom_sentencizer")
def custom_sentencizer(doc):
    for i, token in enumerate(doc[:-2]):
        # Define sentence start if pipe + titlecase token
        if token.text == "|" and doc[i + 1].is_title:
            doc[i + 1].is_sent_start = True
        else:
            # Explicitly set sentence start to False otherwise, to tell
            # the parser to leave those tokens alone
            doc[i + 1].is_sent_start = False
    return doc

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("custom_sentencizer", before="parser")  # Insert before the parser
doc = nlp("This is. A sentence. | This is. Another sentence.")
for sent in doc.sents:
    print(sent.text)

print([token.dep_ for token in doc])
print('---------------')

nlp1 = spacy.load("en_core_web_sm")
# nlp.add_pipe("custom_sentencizer", before="parser")  # Insert before the parser
doc1 = nlp1("This is. A sentence. | This is. Another sentence.")
for sent in doc1.sents:
    print(sent.text)

print([token.dep_ for token in doc1])

print('---------------')

@Language.component("custom_sentencizer1")
def custom_sentencizer1(doc):
    for i, token in enumerate(doc[:-2]):
        # Define sentence start if pipe + titlecase token
        if token.text == "|" and doc[i + 1].is_title:
            doc[i + 1].is_sent_start = True
        # else:
        #     # Explicitly set sentence start to False otherwise, to tell
        #     # the parser to leave those tokens alone
        #     doc[i + 1].is_sent_start = False
    return doc

nlp2 = spacy.load("en_core_web_sm")
nlp2.add_pipe("custom_sentencizer", before="parser")  # Insert before the parser
doc2 = nlp2("This is. A sentence. | This is. Another sentence.")
for sent in doc2.sents:
    print(sent.text)

print([token.dep_ for token in doc2])

