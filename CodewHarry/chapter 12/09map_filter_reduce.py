#MAP

from functools import reduce


l = [ 1, 2, 3, 4]
square = lambda x: x*x

sqList = map(square , l)
print(list(sqList))

#filter example

def even(n):
    if (n%2 ==0):
        return True
    return False
onlyEven = filter(even , l)
print(list(onlyEven))

#Reducr example

def sum(a,b):
    return a+b

print(reduce(sum,l))
