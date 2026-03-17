m=int(input("enter marks for maths: "))
p=int(input("enter marks for physics: "))
c=int(input("enter marks for chem: "))
e=int(input("enter marks for english: "))
a=int(input("enter marks for arts: "))

avg =  (m+p+c+e+a)/5
print(avg)
if(avg>=95):
    print("A+ GRADE WITH MERIT")
elif(avg<95 and avg>=90):
    print("A GRADE")
elif(avg<90 and avg>=80):
    print("B GRADE")    
elif(avg<80 and avg>=70):
    print("C GRADE")    
elif(avg<70 and avg>=60):
    print("D GRADE")    
else:
    print("fail")

