import random
from words import words

def get_valid_word(words):
    word = random.choice(words)
    word = ''.join([x for x in word if str(x).isalnum()])
    return(word)


print(get_valid_word(words))