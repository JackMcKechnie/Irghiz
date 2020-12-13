from Irghiz import get_anglis
from scraping import le_monde

lemonde = le_monde()

for article in lemonde:
    print(get_anglis(article))
    print("")
