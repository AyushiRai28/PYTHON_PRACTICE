# find factorial using loop
# 5! = 1 x 2 x 3 x 4 x 5

n = int(input("Enter a number: "))
product = 1
for i in range(1,n+1):
    product = product * i
    print(f" factorial of {n} is {product}")