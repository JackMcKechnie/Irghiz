from Irghiz import get_anglis
from scraping import le_monde
from tweet import tweet_list

def get_todays(source):

    todays_anglis = []
    for article in lemonde:
        article_anglis = get_anglis(article[0])
        for word in article_anglis:
            if word not in todays_anglis:
                todays_anglis.append(word)
                print(word, article[1], article[2])
                print("")

    return todays_anglis

print("Polling Le Mode...")
lemonde = le_monde()
print("Done")
print("Getting Anglicisms...")
todays = get_todays(lemonde)
print("Done")
#print("Tweeting...")
#tweet_list(todays)
print("Done, successful exit!")
