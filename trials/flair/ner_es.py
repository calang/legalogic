from flair.data import Sentence
from flair.models import SequenceTagger

# load tagger
tagger = SequenceTagger.load("flair/ner-spanish-large")

# make example sentence
# sentence = Sentence("George Washington fue a Washington")
# sentence = Sentence("ARTÍCULO 3º.- Nadie puede arrogarse la soberanía; el que lo hiciere cometerá el delito de traición a la Patria.")
# sentence = Sentence("ARTÍCULO 4º.- Ninguna persona o reunión de personas puede asumir la representación del pueblo, arrogarse sus derechos, o hacer peticiones a su nombre. La infracción a este artículo será sedición.")
sentence = Sentence("""
ARTÍCULO 5º.- El territorio nacional está comprendido entre el Mar Caribe, el Océano Pacífico y las Repúblicas de Nicaragua y Panamá. Los límites de la República son los que determina el Tratado Cañas - Jerez de 15 de abril de 1858 Tratado de Límites entre Nicaragua y Costa Rica (Tratado Cañas-Jerez) , ratificado por el Laudo Cleveland de 22 de marzo de 1888 Laudo Arbitral Cleveland sobre Cuestión de Límites con Nicaragua  con respecto a Nicaragua, y el Tratado Echandi Montero - Fernández Jaén de 1º de mayo de 1941 en lo que concierne a Panamá.
""")
# predict NER tags
tagger.predict(sentence)

# print sentence
print(sentence)

# print predicted NER spans
print('The following NER tags are found:')
# iterate over entities and print
for entity in sentence.get_spans('ner'):
    print(entity)
