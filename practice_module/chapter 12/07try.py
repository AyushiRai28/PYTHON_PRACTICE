# try with else : if code run successfully , it goes in else

try:
    a = int(input("hey enter a number: " ))

    print(a)

except ValueError as v:
    print("heyy")    
    print(v)

except Exception as e:
    print(e)

else:
    print("i am inside else")


#try with finally : ye chlega ho chalega

try:
    a = int(input("hey enter a number: " ))

    print(a)

except ValueError as v:
    print("heyy")    
    print(v)

except Exception as e:
    print(e)

finally:
    print("i am inside finally")
