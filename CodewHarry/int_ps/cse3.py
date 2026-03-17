#ACCEPT COEFF A,B,C OF QUADRATIC EQ AND DETERMINE THE NATURE OF ROOOTS
a = int(input("enter the coefficient of x^2 (a): "))
b = int(input("enter the coefficient of x (b): "))
c = int(input("enter the constant term (c): "))
d = b**2-4*a*c
if(d>0 ):
    print("Roots are real and unequal")
elif(d==0):
    print("Roots are real and equal") 
else: 
    print("Roots are imaginary")      

