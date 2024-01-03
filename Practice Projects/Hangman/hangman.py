'''
Implementation of Hangman by Abdessamad Touzani

YouTube Katsky Studio: https://www.youtube.com/@katskystudio
Medium Abdessamad Touzani: https://medium.com/@abdessamadtouzani
Twitter (X) @at9kat: https://twitter.com/at9kat 
Instagram @t___abdessamad__: https://www.instagram.com/t___abdessamad__/
Website: https://katskydio.wordpress.com/ or directly links: https://lnk.bio/katskystudio
Github: https://www.github.com/AbdessamadTzn

'''
import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words) #randomly choose from words list
    while '-' in word or ' ' in word:
        word = random.choice(words) #we want valid word

    
    return word.upper() #for ease work

def play_hangman():
    word = get_valid_word(words)
    word_letters = set(words) #get the letters in selected word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #for the hangman game, what user has guessed

    lives = 7 #hangman game...limited repetition

    while len(word_letters) > 0 and lives > 0:
        print('You have', lives,' lives left, and you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess the word, enter  letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            
            else:
                lives = lives - 1
                print(f'\nYour letter {user_letter}, isn\'t in the word')

        elif user_letter in used_letters:
            print(f'\nYou have already used the letter {user_letter}...')
        else:
            print('\nYou must enter a valid letter!')

    if lives == 0:
            print(f'Oops...you died! the word was: {word}')
    else:
            print(f'YAAY! You guessed the correct word: {word}')
        
    

play_hangman()
