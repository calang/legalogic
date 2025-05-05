from spacy.lang.en import English

class CustomEnglishDefaults(English.Defaults):
    stop_words = set(["custom", "stop"])

class CustomEnglish(English):
    lang = "custom_en"
    Defaults = CustomEnglishDefaults

nlp1 = English()
nlp2 = CustomEnglish()

print(nlp1.lang, [token.is_stop for token in nlp1("custom stop")])
print(nlp2.lang, [token.is_stop for token in nlp2("custom stop")])
