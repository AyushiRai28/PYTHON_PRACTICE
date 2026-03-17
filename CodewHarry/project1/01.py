# n = int(input("Enter the number :"))

# for i in range(1, n+1):
#     print(" "*(n-i) ,end='')
#     print("*"*(2*i- 1))

# for i in range(0,n+1):
#     print("*"*(n-i) )
     
    
def rem(l, w):
    n=[]
    for  item in l:
        if (item==w):
            n.append(item.strip(w))
    return n 
    
l = ["ayushi","anushree", "anushka", "ayaan", "harry", "an"]
print(rem(l,"an"))