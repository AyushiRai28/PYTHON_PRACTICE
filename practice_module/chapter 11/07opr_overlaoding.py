''' 
operators in python can be overloaded usin dunder methods

the method are called when a given operator is used on the object
__add__
__sub__
__mul__
__truediv__
__floordiv__
__str__
__len__
'''

class Number:
    def __init__(self,n):
        self.n = n


    def __add__(self, num):
            return self.n + num.n
    

n = Number(1)
m = Number(2)

print(n+m)
