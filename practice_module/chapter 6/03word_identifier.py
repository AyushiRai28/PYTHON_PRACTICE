p1 = "make money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click link"

msg = input("enter your message: ")

if((p1 in msg) or (p2 in msg) or (p3 in msg) or (p4 in msg)):
    print("This is a scam msg")
    print("Beware!!!")


else:
    print("this is not a scam msg")    

    # "in" keyword is used to know whether a letter is present in a input or not
    # example a = "ayushi is here"
    # ayushi in a = true