# write a program to print a star pattern
'''  
  *
 ***
***** for n = 3
'''

n = int(input(" Enter a number : "))

for i in range(1,n+1) :
    print(" " * (n-i),  end="")
    print("*"* (2*i-1) , end="")
    print("")
    

'''  
*
***
***** for n = 3
'''
 
o = int(input("enter a number: "))
for i in range(1,o+1):
    print("*" * (2*i-1), end="")
    print("")


''' 
for n = 3
***
* *
***
'''

p = int(input("Enter a number : "))
for i in range(1, p+1):
    if(i==1 or i==p):
        print("*"*p,end="") 
        print("")

    else:
        print("*",end="")
        print(" "*(p-2), end="")
        print("*",end="")
        print("")
