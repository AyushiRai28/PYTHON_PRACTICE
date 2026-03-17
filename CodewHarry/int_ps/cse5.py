b = int(input("enter your balance: "))
a = int(input("enter your amount to withdraw: "))

if(a<=b and a%100==0):
    print("AMOUNT WITHDRAWED")
elif( a%100>0):
    print("invalid withdraw")
else:
    print("insufficient funds")        

'''
if (a<=b):
    if(a%100==0):
        print("WITHDRAW SUCCESS")
    else:
        print("invalid wuthdraw")
else:
    print("Insufficient")
 '''  
