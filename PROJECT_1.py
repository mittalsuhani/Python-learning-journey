import random

x=random.randint(1,100)

print("welcome to the number guessing game!")
print("i have selected a number between 1 and 100. can you guess it?")
while True:
    guess=int(input("Enter a number "))
    if guess==x:
        print("CONGRATULATIONS YOU GUESSED IT CORRECTLY")
        break
    elif guess>x:
        print("too high")
    else:
        print("too low")