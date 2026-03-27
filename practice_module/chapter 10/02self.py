class employee :
    name = "harry"
    language = "py"
    salary = 200000

    def getInfo(self):
        print(f"The language is {self.language}. the salary is {self.salary}")
    

    @staticmethod
    def greet():
        print("Good morning")

    # by using @staticmethod , we told pythoon that it doesn't contain any object , hence self not needed.  

harry = employee()
harry.getInfo() # or employee.getinfo(harry)   
# harry is the "self" argument

