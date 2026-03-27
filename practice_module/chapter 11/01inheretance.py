# if we have to make many classes with slight changes , instead of copy paste and editing , we can inherit
'''
Employee is the base class
programmer is the derived class'''
class Employee :
    company = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.name } amd the salary is a{self.salary}")


class programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")

a = Employee()
b = programmer()  

print(a.company , b.company)