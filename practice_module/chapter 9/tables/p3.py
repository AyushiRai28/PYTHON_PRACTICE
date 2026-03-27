# write a program to print table of  given numbers 
# and write it to the different files. place tjese files in a folder
def generatetable(n):
    table = "" 
    for i in range(1,11):
        table += f"{n} X {i} = {n*i} \n "

    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)   
for i in range(15, 21) :
    generatetable(i)       