import time
from flair.data import Sentence
from flair.nn import Classifier

# make a sentence
# sentence = Sentence('George Washington went to Washington.')
sentence = Sentence(
    """
    ARTÍCULO 5º.- El territorio nacional está comprendido entre el Mar Caribe, el Océano Pacífico y las Repúblicas de Nicaragua y Panamá. Los límites de la República son los que determina el Tratado Cañas - Jerez de 15 de abril de 1858 Tratado de Límites entre Nicaragua y Costa Rica (Tratado Cañas-Jerez) , ratificado por el Laudo Cleveland de 22 de marzo de 1888 Laudo Arbitral Cleveland sobre Cuestión de Límites con Nicaragua  con respecto a Nicaragua, y el Tratado Echandi Montero - Fernández Jaén de 1º de mayo de 1941 en lo que concierne a Panamá.
    """
)

# load the NER tagger
tagger = Classifier.load('ner-large')

start = time.time()

# run NER over sentence
tagger.predict(sentence)

stop = time.time()

# print the sentence with all annotations
print(sentence)
print(f"Time: {stop - start} s")
