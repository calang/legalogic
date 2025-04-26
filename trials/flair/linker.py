"""
As of Flair 0.12 we ship an experimental entity linker trained on the Zelda dataset.
The linker does not only tag entities, but also attempts to link each entity
to the corresponding Wikipedia URL if one exists.
"""

from flair.nn import Classifier
from flair.data import Sentence

# load the model
tagger = Classifier.load('linker')

# make a sentence
sentence = Sentence('Kirk and Spock met on the Enterprise.')

# predict entity links
tagger.predict(sentence)

# iterate over predicted entities and print
for label in sentence.get_labels():
    print(label)
