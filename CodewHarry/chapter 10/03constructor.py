''' 
dunder method = mrthods ehich starts with undersscore
_init_ is dunder method ehich is called automatically

'''
class employee :
    name = "harry"
    language = "py"
    salary = 200000

    def __init__(self, name , salary, language):
        self.name = name
        self.salary = salary
        self.language = language


#CALLING THE CLASS

harry = employee("harry",1300000 , "java")
print(harry.name , harry.salary, harry.language)

          
