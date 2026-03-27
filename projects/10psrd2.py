import random
import string

def generate_password(length):
    characters = 0
    if upper == 'y' and lower =='y' and number == 'y' and character == 'y':   
        characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    elif upper == 'y' and lower =='y' and number == 'y' and character == 'n':   
        characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    elif upper == 'y' and lower =='y' and character == 'y' and number == 'n' :   
        characters = string.ascii_uppercase + string.ascii_lowercase + string.punctuation
    elif upper == 'y'  and number == 'y' and character == 'y' and lower =='n':   
        characters = string.ascii_uppercase + string.digits + string.punctuation
    elif lower =='y' and number == 'y' and character == 'y' and upper == 'n' :   
        characters =  string.ascii_lowercase + string.digits + string.punctuation
    elif lower =='y' and number == 'y' and character == 'n' and upper == 'n' :   
        characters =  string.ascii_lowercase + string.digits 
    elif lower =='y' and number == 'n' and character == 'y' and upper == 'n' :   
        characters =  string.ascii_lowercase + string.punctuation
    elif lower =='n' and number == 'y' and character == 'y' and upper == 'n' :   
        characters =  string.digits + string.punctuation
    elif lower =='n' and number == 'n' and character == 'y' and upper == 'y' :   
        characters =  string.ascii_uppercase + string.punctuation
    elif lower =='n' and number == 'y' and character == 'n' and upper == 'y' :   
        characters =  string.ascii_uppercase + string.digits 
    elif lower =='y' and number == 'n' and character == 'n' and upper == 'y' :   
        characters =  string.ascii_lowercase + string.ascii_uppercase
    elif lower =='y' and number == 'n' and character == 'n' and upper == 'n' :   
        characters =  string.ascii_lowercase 
    elif lower =='n' and number == 'n' and character == 'n' and upper == 'y' :   
        characters =  string.ascii_uppercase
    elif lower =='n' and number == 'y' and character == 'n' and upper == 'n' :   
        characters =  string.ascii_digits
    elif lower =='n' and number == 'n' and character == 'y' and upper == 'n' :   
        characters =  string.ascii_punctuation
    else :
        print("invalid ")
        print("Try again !!")
        

    
    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password

# user input
length = int(input("Enter password length: "))

upper = input("Include uppercase letter? (y/n)")
lower = input("Include lowercase letter? (y/n)")
number = input("Include numbers ? (y/n)")
character = input("Include special character ? (y/n)")

print("Generated Password:", generate_password(length))




'''  

import random
import string

def generate_password():
    print("===== PASSWORD GENERATOR =====")

    length = int(input("Enter password length: "))

    use_upper = input("Include uppercase letters? (y/n): ").lower()
    use_numbers = input("Include numbers? (y/n): ").lower()
    use_special = input("Include special characters? (y/n): ").lower()

    characters = string.ascii_lowercase  # always include lowercase

    if use_upper == 'y':
        characters += string.ascii_uppercase

    if use_numbers == 'y':
        characters += string.digits

    if use_special == 'y':
        characters += string.punctuation

    if not characters:
        print("Error: No character types selected!")
        return

    password = "".join(random.choice(characters) for _ in range(length))

    print("Generated password:", password)

# Run the program
generate_password()


'''



