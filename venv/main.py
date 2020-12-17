from Irghiz import get_anglis
from scraping import le_monde
from tweet import tweet_list
from update_git import update_md


def get_todays(source):

    todays = []
    for article in lemonde:
        article_anglis = get_anglis(article[0])
        for word in article_anglis:
            if word not in todays:
                todays.append((word, article[2]))
    return todays

print("Polling Le Monde...")
lemonde = le_monde()
print("Done")

print("Getting Anglicisms...")
todays = get_todays(lemonde)
print("Done")

print("Updating MD file...")
to_be_tweeted = update_md(todays)
print("Done")

print("Tweeting")
tweet_list(to_be_tweeted)
print("Done")

print("Done, successful exit!")
