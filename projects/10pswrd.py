'''
Write a program to evaluate the strength of a password based on criteria like
length, the inclusion of uppercase letters, numbers, and special characters. The
program will then categorize the password as Very Weak, Weak, Medium, Strong,
or Very Strong.

list1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
         'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
         'u', 'v', 'w', 'x', 'y', 'z']

list3 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
         'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
         'U', 'V', 'W', 'X', 'Y', 'Z']

list4 = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
         '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',
         ';', ':', "'", '"', ',', '.', '<', '>', '/', '?', '`', '~']
'''
#import getpass    getpass.getpass("Enter a password: ") hides it all, no * 



while True:
    user = input("Enter a password: ")
    number = 0
    lower = 0
    upper = 0
    character = 0

    for i in user:
        
        if i.isdigit():
            number += 1
        elif i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
        else:
            character += 1


    if len(user)< 8:
        print("Keep the length above 8 characters.")
        continue


    if number == 0 or lower == 0 or upper == 0 or character == 0:
        print("Very weak Password!")
        print("Please include:\n- Uppercase\n- Lowercase\n- Special character\n- Digit")
        continue

    if number >= 1 and lower >= 1 and upper >= 1 and character >= 1:
        print("Strong Password")
        break
        

print("Your password has been updated successfully")

