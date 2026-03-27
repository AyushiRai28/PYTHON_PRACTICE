# write a program  to convert a celsius into fahrenheit

# c/5 = (f-32)/9
'''
c = int(input(" enter the temperature in celsius : "))

f= 9/5*c + 32
print(f)
'''
#   write using functions
 
c = int(input("Enter temp in celsius:"))
def func(c):
    return (32 + (c) * 9/5)
print(f" the value of temp in fahrenheit is: {func(c)} ")

#you can also use round of function
# round(c(f), 2) which means to rounf of the value of c(f) upto 2 decimal places


