# write a class "calculator " capable of finding square, cube and square root of a number

class Calculator:
    def __init__(self,n):
        self.n = n

    def square(self):
            print(f" square is {self.n*self.n}")

    def cube(self):
            print(f" cube is {self.n*self.n*self.n}")

    def sqrroot(self):
            print(f" square root is {self.n**0.5}")


a = Calculator(4)            
a.square()
a.cube()
a.sqrroot()