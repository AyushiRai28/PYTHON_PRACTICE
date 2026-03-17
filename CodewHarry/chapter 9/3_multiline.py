#multiple lines

f = open("file.txt")
line = f.readlines()
print(line , type(line))
line1 = f.readline()
print(line1, type(line1))
line2 = f.readline()
print(line2, type(line2))

# line = f.readline()
# while (line !=""):
#     print(line)
#     line =  f.readline


f.close