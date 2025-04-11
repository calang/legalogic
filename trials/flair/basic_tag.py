# The sentence objects holds a sentence that we may want to embed or tag
from flair.data import Sentence

# Make a sentence object by passing a string
sentence = Sentence('The grass is green.')

# Print the object to see what's in there
print(sentence)


for token in sentence:
    print(token)


# using the token id
print(sentence.get_token(4))
# using the index itself
print(sentence[3])


# Make a sentence object by passing a string
sentence = Sentence('The grass is green.')

# add an NER tag to token 3 in the sentence
sentence[3].add_label('ner', 'color')

# print the sentence (now with this annotation)
print(sentence)


sentence = Sentence('The grass is green.')

# add a label to a sentence
sentence.add_label('sentiment', 'POSITIVE')

print(sentence)


# iterate over all labels and print
for label in sentence.get_labels():
    print(label)