from flair.nn import Classifier
from flair.data import Sentence

# load the model
tagger = Classifier.load('pos')

# make a sentence
sentence = Sentence('Dirk went to the store.')

# predict NER tags
tagger.predict(sentence)

# print sentence with predicted tags
print(sentence)
