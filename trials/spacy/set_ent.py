import spacy
from spacy.tokens import Span

nlp = spacy.load("en_core_web_sm")
doc = nlp("fb is hiring a new vice president of global policy")
ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
print('Before', ents)
# The model didn't recognize "fb" as an entity :(

# Create a span for the new entity
fb_ent = Span(doc, 0, 1, label="ORG")
orig_ents = list(doc.ents)

# Option 1: Modify the provided entity spans, leaving the rest unmodified
doc.set_ents([fb_ent], default="unmodified")

# Option 2: Assign a complete list of ents to doc.ents
doc.ents = orig_ents + [fb_ent]

ents = [(e.text, e.start, e.end, e.label_) for e in doc.ents]
print('After', ents)
# [('fb', 0, 1, 'ORG')] 🎉
