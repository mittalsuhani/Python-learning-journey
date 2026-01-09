#project 2 is a simple calculator that performs basic arithmetic operations
#functions to perform addition,subtraction,multiplication and division
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y==0:
        return "Error! Division by zero."
    return x/y  

#from here starts the main program

print("Welcome to the Simple Calculator!")

while True:
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    print("Select operation:")  
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")    
    print("4. Divide")
    print("5. Exit")
    choice=input("enter your choice(1/2/3/4): ")
    match choice:
        case '1':
            
            print(f"{num1} + {num2} = {add(num1,num2)}")    #here i have used the concept of f-strings to format the output
        case '2':
            
            print(f"{num1} - {num2} = {subtract(num1,num2)}")
        case '3':
           
            print(f"{num1} * {num2} = {multiply(num1,num2)}")
        case '4':
           
            print(f"{num1} / {num2} = {divide(num1,num2)}")
        case '5':
            print("Exiting the calculator....")
            break
        case _:
            print("Invalid input")