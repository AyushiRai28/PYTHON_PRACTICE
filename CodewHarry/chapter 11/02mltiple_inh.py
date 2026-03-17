class Employee :
    company = "ITC"
    salary = 1200000
    def show(self):
        print(f"The name of the Employee is {self.company} amd the salary is {self.salary}")
class Coder :
    language = "Python"
    def printLanguage(self):
        print(f"Out of all the languages here is your langauge : {self.language}")

class programmer(Employee , Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")

a = Employee()
b = programmer()  

b.show()
b.printLanguage()
b.showLanguage()          