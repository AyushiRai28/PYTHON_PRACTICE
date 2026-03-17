# write a program to find sun of first n natural numbers

n = int(input(" Enter the number you want sum of : "))

def sum(n) :
    if(n==1):
        return 1

    return n + sum(n-1)
print(sum(n))