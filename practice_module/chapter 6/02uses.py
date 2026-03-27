# write a program to  find the greatest number out of 4 numbers

a = int(input("Enter number 1 : "))
b = int(input("Enter number 2 : "))
c = int(input("Enter number 3 : "))
d = int(input("Enter number 4 : "))

if(a>b and a>c and a>d) :
    print(" number 1 is greatest of all" , a)

elif(b>a and b>c and b>d) :
    print(" number 2 is greatest of all", b)

elif(c>b and c>a and c>d) :
    print(" number 3 is greatest of all", c)

elif(d>b and d>c and d>a) :
    print(" number 4 is greatest of all", d)

elif(a==b or a==c or a==d or b==c or b==d or c==d) :
    print("sorry you have entered two or more equal values")

print("end of the program")