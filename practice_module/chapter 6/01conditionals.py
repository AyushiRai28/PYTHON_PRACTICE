# if elif else ladder

n = int(input("Enter your age : "))
if(n%2==0):
    print("n is even")
if(n>18):
    print("you are above the age of consent")
    print("good for you")

elif(n<0):
    print("entered data is incorrect")


else : 
    print("you are below the age of consent")
    print("sooo sad")
    

#mutiple if can be used , the elif and else condition applies to the last applied if
# multiple elif can  be used but not else  