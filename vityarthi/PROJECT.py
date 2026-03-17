print("HELLO USER!!")
print("            WELCOME TO DUMPLIN UNIIVERSITY               ")
print(" This page is made of collecting the students/teachers data, and providing them the information about their schedule. ")

pcm = [ 'MATHS', 'PHYSICS','CHEMISTRY','ENGLISH','COMPUTER APPLICATIONS',]
pcb = ['PHYSICS', 'CHEMISTRY', 'BIOLOGY', 'ENGLISH', 'PHYSICAL EDUCTIONS',]
arts = ['HISTORY','GEOGRAPHY', 'POLITICAL SCIENCE', 'PSYCHOLOGY/PHYSICAL EDUCATIONS', 'ENGLISH',]
commerce = ['ACCOUNTANCY', 'BUISINESS STUDIES', 'ECONOMICS','ENGLISH', 'PHYSICAL EDUCATION',]
type=input("Enter user type(student/faculty):")
if type.lower()=='student':
    print("WELCOME STUDENT")
    name =input("Enter name:")
    age =int(input("Enter age:"))
    while age<=00:
        print("Invalid age")
        print("Try again")
        age =int(input("Enter age:"))


    gender =input("Enter gender:")

    phone =int(input("Enter phone number:"))
    if len(str(phone))!=10:
        print("Invalid phone number")

    f_name =input("Enter fathers name:")
    m_name =input("Enter mothers name:")
    adress =input("Enter your adress:")
    stream =input("Enter your stream:")
    print("WELCOME TO THE STUDENT MANAGEMENT SYSTEM")
    print(" -----PERSONAL INFORMATION-----")
    print("Name:",name)
    print("Age:",age)
    print("Gender:",gender)
    print("Stream:",stream)
    print("Phone:",phone)

    print("Father's name:",f_name)
    print("Mother's name:",m_name)
    print("Adress:",adress)
    print(" -----SUBJECTS-----")
    if stream.upper()=='PCM':
        for i in pcm:
            print(i)
    elif stream.upper()=='PCB':
        for i in pcb:
            print(i)
    elif stream.upper()=='ARTS' :
        for i in arts:
            print(i)
    elif stream.upper()=='COMMERCE':
        for i in commerce:
            print(i)
    else:
        print("Invalid stream")


elif type.lower()=='faculty':
    name =input("Enter name:")
    age =int(input("Enter age:"))
    while age<=00:
        print("Invalid age")
        print("Try again")
        age =int(input("Enter age:"))

    gender =input("Enter gender:")
    subject =input("Enter subject:")
    phone =int(input("Enter phone number:"))
    if len(str(phone))!=10:
        print("Invalid phone number")

    adress =input("Enter your adress:")
    print("WELCOME TO THE FACULTY MANAGEMENT SYSTEM")
    print(" -----PERSONAL INFORMATION-----")
    print("Name:",name)
    print("Age:",age)
    print("Gender:",gender)
    print("Subjet to teach:",subject)
    print("Phone:",phone)

    print("Adress:",adress)
    print("Adress:",adress)

    print(" -----SLOTS-----")
    print("Kindly contact the office")

else:
    print("Invalid user type")


exam=input("do you want examination info(yes/no) :")
if exam.lower()=='yes':
    print("HERE IS YOUR EXAM SCHEDULE")
    print(" -----EXAMINATION SCHEDULE-----")
    e = {'e_pcm':{ 'mathematics:': '2 january', 'physics: ': '3 january', 'chemistry: ': '4 january', 'english: ': '5 january', 'computer applications: ': '6 january',},
    'e_pcb' :{'physics: ' : '2 january', 'chemistry: ': '3 january', 'biology: ': '4 january', 'english: ': '5 january', 'physical eductions: ': '6 january',},
    'e_arts' : {'history: ': '2 january', 'geography: ': '3 january', 'political science: ': '4 january', 'psychology/physical eductions: ': '5 january', 'english: ': '6 january',},
    'e_commerce' : {'accountancy: ': '2 january', 'buisiness studies: ': '3 january', 'economics: ': '4 january', 'english: ': '5 january', 'physical education: ': '6 january',},
    }
    for i,j in e.items():
        print(i)
        for k,l in j.items():
            print(k,l)



    print("              -EXAM ELIGIBILITY CRITERIA-           ")
    criteria={ 'attendance:':'75% and more' , 'midterm marks: ':' 30  or more' , 'previous grade: ':'A / B / C /D' }
    for i,j in criteria.items():
        print(i,j)
else :
  print(" THANK YOU !!")

