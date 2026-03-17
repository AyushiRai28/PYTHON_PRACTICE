# write a program to find whether a name is present in a list or not

l = (" Hey my name is Ayushi Rai")

i = input(" enter your word : ")
 
if(i.lower() in l.lower() ): # text.lower used to convert all in lower case and then find 
 print("given word present")

else:
 print("not present")  