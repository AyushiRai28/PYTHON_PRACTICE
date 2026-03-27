# write a program using funvtions to find the greatest of 3 numbers


def greatest(a, b, c) :
    if( a>b and a>c):
        return a
    
    elif(b>c and b>a):
        return b
    
    elif(c>a and c>b):
        return c
    
a = 1
b = 2
c = 3

        
print(greatest(a, b, c))


    