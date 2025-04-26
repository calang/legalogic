from flair.nn import Classifier
from flair.splitter import SegtokSentenceSplitter

# example text with many sentences
text = "Bayern played against Barcelona. The match took place in Barcelona."

# initialize sentence splitter
splitter = SegtokSentenceSplitter()

# use splitter to split text into list of sentences
sentences = splitter.split(text)

# predict tags for sentences
tagger = Classifier.load('linker')
tagger.predict(sentences)

# iterate through sentences and print predicted labels
for sentence in sentences:
    print(sentence)
