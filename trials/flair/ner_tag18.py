import time

from flair.data import Sentence
from flair.nn import Classifier

from trials.flair.best_tag import start

# make a sentence
# sentence = Sentence('On September 1st George won 1 dollar while watching Game of Thrones.')
sentence = Sentence('El primero de septiembre Chepito se ganó $1 mientras miraba Juego de Tronos.')

# load the NER tagger
tagger = Classifier.load('ner-ontonotes-large')

start = time.time()
# run NER over sentence
tagger.predict(sentence)
stop = time.time()

# print the sentence with all annotations
print(sentence)
print(f"Time: {stop - start} s")
