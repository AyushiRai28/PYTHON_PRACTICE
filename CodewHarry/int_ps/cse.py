# atm pin verification, allow 3 attempt . if correct  - access  granted, else card blocked

pin = 1234

p=int(input("enter your pin: "))
if( p==pin):
    print("ACCESS GRANTED")
else:
    p1=int(input("enter pin: "))

    if(p1==pin):
        print("ACCESS GRANTED")
    else:
        p2=int(input("enter last attempt pin: ")) 
        if(p2==pin):
            print("ACCESS GRANTED")
        else:
            print("CARD BLOCKED")    
    