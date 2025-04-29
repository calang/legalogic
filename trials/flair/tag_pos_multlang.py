from flair.nn import Classifier
from flair.data import Sentence

# load model
tagger = Classifier.load('pos-multi')

# text with English and German sentences
sentence = Sentence('''
George Washington went to Washington.
Dort kaufte er einen Hut.
Chepe se baña.
Chepe bañó al perrito.
''')

# predict PoS tags
tagger.predict(sentence)

# print sentence with predicted tags
print(sentence)