# in which line the word is present 
with open("file.txt") as f :
    lines = f.readlines()
lineno = 1
for line in lines :
    if ("i" in line):
        print (f" yes -i- is present in line {lineno}")
        break
    lineno += 1
else :
     print ("not present")
    