# types of functions  - built inn function and user defined function
# built in = len() ,print() etc      user defined = function1()


def goodDay(name , ending):
    print("Good Day , " + name )
    print(ending)

goodDay("Ayushi" , "thank you")    
goodDay("Ayush", "thnku")    
goodDay("Ayus", "thnks")    
goodDay("Ayu", "tq")    
    


 # return function = tells function to have a value and give it to a variable
def hlo(name):
   print("Hello ," , name)
   return "OKKAY"

a = hlo("Ayushi")
print(a) # return is the value of a


#to block a new line end="" is used    example= print("hello " ", end="")
