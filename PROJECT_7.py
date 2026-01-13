#project 7 is a rock-paperscissors game
#it uses basic concepts of functions and conditionals
#core idea is that the user plays against the computer
import random

def comp_choice():
    choices=['rock','paper','scissors']
    return random.choice(choices)

def find_winner(user,comp):
    if (user==comp):
        print("It's a tie!")
        return
    elif (user=='rock' and comp=='scissors') or (user=='paper' and comp=='rock') or (user=='scissors' and comp=='paper'):
        print("You win!")
        return
    else:
        print("Computer wins!")
        return
    
while True:
    print("Welcome to Rock-Paper-Scissors Game!")
    user=input("Enter rock, paper, or scissors (or 'quit' to exit): ")
    user=user.lower()
    if (user=='quit'):
        break
    if user not in ['rock','paper','scissors']:
        print("Invalid choice, please try again.")
        continue
    comp=comp_choice()
    print(f"Computer chose: {comp}")
    find_winner(user,comp)
    