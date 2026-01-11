#project 4 is a password strength checker
# it uses basic concepts of strings and conditionals
#the core idea is that the user will input a password 
# and the program will evaluate its strength based on length and character variety

def check_password_strength(password):
    if(len(password) < 8):
        print("Weak: Password is too short. Minimum 8 characters required.")
        return 
    elif(len(password) > 25):
        print("password is too long. Maximum 25 characters allowed.")
        return 
    
    upper_count = 0
    lower_count = 0
    digit_count = 0
    special_count = 0

    for char in password:
        if char.isupper():  #checks if the character is uppercase
            upper_count += 1
        elif char.islower():  #checks if the character is lowercase
            lower_count += 1
        elif char.isdigit():   #checks if the character is a digit
            digit_count += 1
        else:
            special_count += 1    #if the character is none of the above, it is considered special

    if(upper_count > 0 and lower_count > 0 and digit_count > 0 and special_count > 0):
        print("Strong: Password contains uppercase, lowercase, digits, and special characters.")
    elif( lower_count > 0 and digit_count > 0 and special_count > 0) or (upper_count > 0 and lower_count > 0 and special_count > 0) or (upper_count > 0 and digit_count > 0 and special_count > 0) or (upper_count > 0 and lower_count > 0 and digit_count > 0):
        print("Moderate strength.")
    else:
        print("Weak: Password lacks variety in character types.")
# Get user input
user_password = input("Enter your password (8-20 length) to check its strength: ")    
strength = check_password_strength(user_password)

