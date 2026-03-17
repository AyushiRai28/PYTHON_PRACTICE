''' recursion is a function that calls itself
it is used to directly use a mathematical formula as a funtion 

let say 
factorial(1) = 1
factorial(2) = 2 x 1
factorial(3) = 3 X 2 x 1
factorial(4) = 4 X 3 X 2 x 1
factorial(5) = 5 X 4 X 3 X 2 x 1
.
.
.
factorial(N) = N X N-1 X .... 3 X 2 x 1
factorial(n) = n * factorial(n-1)
write it as a function
'''

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input(" Enter a number : "))
print( f" The factorial of the number is , {factorial(n)} ")
