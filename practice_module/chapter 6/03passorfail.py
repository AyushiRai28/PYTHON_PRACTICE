#write a program to find whether a student is passed or fail if it need total of 40% and 33% individual in all subject

p = int(input(" Enter your marks in pysics out of hundred  : "))
c = int(input(" Enter your marks in chemistry out of hundred : "))
m = int(input(" Enter your marks in maths out of hundred : "))

total_percentage = (100*(p+c+m))/300

if(total_percentage>=40 and p>=33 and c>=33 and m>=33):
    print(" You passed the exam " \
    "your percentage is:", total_percentage)


else:
    print(" sorry you failed " \
    "your  percentage is:",  total_percentage)    




print("Thank You")    
