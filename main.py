import re
def censor(file, word):
    result = re.sub(word, '*' * len(word), file)
    return result
file = "Если вы живете жизнь, которая обогащает духовно еще и жизни окружающих вас людей, значит вы живете великую жизнь."
word = "жизнь"
print(censor(file, word))