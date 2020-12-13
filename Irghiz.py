import enchant
import spacy


# Read in test corpus of F1 Wiki page in French
with open("C:\\Users\\jack-\\PycharmProjects\\Irghiz\\F1WikiFr.txt", "r", encoding='utf-8') as file:
    corpus = file.read().replace('\n', '')

# Use spaCy
nlp = spacy.load("fr_core_news_sm")
doc = nlp(corpus)
nouns = [chunk.text for chunk in doc.noun_chunks]

en_dict = enchant.Dict('en_UK')
fr_dict = enchant.Dict('fr')

out = []

for noun in nouns:
    for word in noun.split():
        if en_dict.check(word) is True and fr_dict.check(word) is False:
            nouns_doc = nlp(word)
            for entity in nouns_doc.ents:
                if entity.label_ != 'ORG' and entity.label_ != 'PER' and word not in out:
                    out.append(word)



