import random
import time


def play():
    valid_user_inputs = ['r', 'p', 's']
    computer = random.choice(['r', 'p', 's'])
    while True:
        try:
            user = input("Your game? 'r' for rock, 'p' for paper and 's' for scisor >> ")
            if user not in valid_user_inputs:
                raise ValueError('Invalid input. PLease enter r, p or s')

            if user == computer:
                return 'Its a Tie!'

            if is_winner(user, computer):
                return "You won!"
            
            return "You lost!"
        except ValueError as e:
            print(e)


def is_winner(player, opponent):
    #r>s, s>p, p>r
    if (player == 'p' and opponent == 'r') or (player=='s' and opponent=='p') \
                or (player == 'r' and opponent == 's'):
        return True
    else:
        return False

if __name__ == '__main__':
    while True:
        print(play())
        wait_time = 3 #set it as need in seconds
        print(f'The game will start again in {wait_time} seconds...ctrl+c to interupt it')
        time.sleep(wait_time)


