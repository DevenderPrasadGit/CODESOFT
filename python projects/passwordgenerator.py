import random
import string

def generate_password(min_length, number=True, special_character=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    character = letters
    if number:
        character+= digits
    if special_character:
        character+=special

    pwd =""
    meets_criteria=False
    has_number= False
    has_special=False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(character)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        
        meets_criteria=True
        if number:
            meets_criteria = has_number
        if special_character:
            meets_criteria = meets_criteria and has_special
    return pwd
min_lenght = int(input("enter the length of the password: "))
has_number = input("do you want number in your password (y/n)? ").lower() == "y"
has_special = input("do you want special characters in your password(y/n)? ").lower()== "y"
pwd=generate_password(min_lenght, has_number, has_special)
print("The generated password is:", pwd)
