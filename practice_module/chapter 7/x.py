n=int(input("enter the number:"))
sum=0
i=1
count=0
temp=n
while n>0:
    n=n//10
    count=count+1
print(count)    

n=temp
while n>0:
    r=n%10
    sum=sum+r*10**(count-i)
    n=n//10
    i=i+1
print("reverse of number is",sum)    