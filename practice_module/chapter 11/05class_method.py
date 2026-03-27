# if we want the class attribute to run and not the instance attribute then we use this
#  it uses cls instead of self

class employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")