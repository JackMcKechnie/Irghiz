from langid.langid import LanguageIdentifier, model
from nltk.util import everygrams

with open("C:\\Users\\jack-\\PycharmProjects\\Irghiz\\F1WikiFr.txt", "r", encoding='utf-8') as file:
    corpus = file.read().replace('\n', '')

identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)
identifier.set_languages(['en', 'fr'])

ngrams = list(everygrams(corpus.split(), max_len=2))

possible_anglis = []

for ngram in ngrams:
    ngram = ' '.join(ngram)
    if identifier.classify(ngram)[1] > 0.97 and identifier.classify(ngram)[0] == 'en' and ngram not in possible_anglis:
        possible_anglis.append(ngram)

for i in possible_anglis:
    print(i)
    print("")





