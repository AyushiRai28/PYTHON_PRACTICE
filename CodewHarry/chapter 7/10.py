# write a program to find if a number is prime number
n = int(input("Enter a nummber: "))
for i in range(2,n):
    if(n%i) == 0: ##% used to know the remainfer of two numbers
        print("Number  is not prime")
        break
else:
    print("number is prime")    