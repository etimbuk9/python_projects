import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    word = ''.join([x for x in word if str(x).isalnum()])
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)

    alphabet = set(string.ascii_lowercase)
    used_letters = set() #what user has guessed

    lives = 6

    while len(word_letters) != 0 and lives != 0:
        #Used Letters
        print('You have',lives,'lives left and You have used these letters: ', ' '.join(used_letters))


        # what the word is 
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ')
    
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print('letter not in word')
        elif user_letter in used_letters:
            print('You have already used this character')
        else:
            print('Invalid character')
    
    if lives != 0:
        print(f'You got the word and it is "{word.upper()}"')
    else:
        print('He died. The word was', word.upper())


if __name__ == '__main__':
    hangman()