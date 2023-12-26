'''
Implementation of number gussing by computer or user, by Abdessamad Touzani

YouTube Katsky Studio: https://www.youtube.com/@katskystudio
Medium Abdessamad Touzani: https://medium.com/@abdessamadtouzani
Twitter (X) @at9kat: https://twitter.com/at9kat 
Instagram @t___abdessamad__: https://www.instagram.com/t___abdessamad__/
Website: https://katskydio.wordpress.com/ or directly links: https://lnk.bio/katskystudio
Github: https://www.github.com/AbdessamadTzn

'''
import random
import time

def guess():
    def user_guess(x):
        random_number = random.randint(1, x)
        guess = 0
        while(guess != random_number):
            guess = int(input(f'Guess a number between 1 and {x}: '))
            if(guess < random_number):
                print("Greather...")
            elif(guess > random_number):
                print("Less...")
            else:
                print(f"Tada...You just guessed the right random number {random_number}!")
            
    def computer_guess(x):
        high = x
        low = 1
        decision = ''

        while decision != 'c':
            guess = random.randint(low, high)
            decision = input(f'Is {guess} you number? (h) too high, (l) too low, (c) right answer: ')
            if decision == 'h':
                high = guess-1
            elif decision == 'l':
                low = guess+1
        print(f'TADA, {guess} is your number')

    guesser = input("Computer guess (c) or You guess (u)?")

    if guesser=='c':
        print("Think for a number, and remember it....\n")
        num = int(input("The low is 1, please enter the high number for guessing range: "))
        computer_guess(num)
    elif guesser == 'u':
        num = int(input("The low is 1, please enter the high number for guessing range"))
        user_guess(num)
if __name__ == '__main__':
    while True:
        guess()
        wait_time = 5
        print(f'Waiting {wait_time} seconds before starting again...')
        time.sleep(wait_time)
