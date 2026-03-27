a = int(input("enter number: "))
b = int(input("enter number: "))

if(b==0):
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")
else :
    
    print(f"the division is {a/b}")