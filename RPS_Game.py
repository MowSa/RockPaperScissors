import random

def play():
    user = input("Rock, Paper or Scissors? ")
    cpu = random.choice(['rock', 'paper', 'scissors'])

    if user == cpu:
        return"It's a tie :/"

    elif check_winner(user, cpu):
        return 'You won! :)'
    
    else :
        return 'You lost! :('

def check_winner(player, opponent):
    if (player == 'rock' and opponent == 'scissors' or player == 'scissors' and opponent == 'paper' or player == 'paper' and opponent == 'rock'):
        return True


print(play())