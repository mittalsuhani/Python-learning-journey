#project 5 is a dice rolling simulator
# it uses basic concepts of random number generation and loops
# the core idea is that the user will specify how many dice to roll

import random 

#function to roll n dice 
def roll_dice(n):
    results=[]  # empty list to store the result of each die roll
    for i in range(n):
        results.append(random.randint(1, 6))
    
    return results

#main function /driver code
n=int(input("Enter the number of dice to roll: "))
if n <= 0:
    print("number of dice must be a positive integer.")
else:
    result=roll_dice(n)
    print(f"Results of rolling {n} dice: {result}")