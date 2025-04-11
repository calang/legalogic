# ValueError: Could not find any model with name 'sentiment-fast'

from flair.nn import Classifier
from flair.data import Sentence

# load the model
tagger = Classifier.load('sentiment-fast')

# make a sentence
sentence = Sentence('This movie is very bad.')

# predict NER tags
tagger.predict(sentence)

# print sentence with predicted tags
print(sentence)
