#info of programmers working in microsoft using class "programmer"

class Programmer :
    company = 'Microsoft'
    def __init__(self,name , salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = Programmer("ayushi", 2400000 , 466112)

print(p.name , p.salary, p.pin)
