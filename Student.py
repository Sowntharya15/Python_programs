
# encapsulation example 
# user- defined datatype = Student 
# getter() and setter()
class Student():
    __name = None
    __age = None
    def set_name(self,name):
        if name.isalpha:
            self.__name = name
        else:
            print("entered name is not valid")   # it will throw error 
            exit()
    def set_age(self,age):
        if age > 5 and age < 30:
            self.__age = age
        else:
            print("entered age is not valid")
            exit()
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
stud1 = Student()
stud1.set_name('yash')
stud1.set_age(20)
print(stud1.get_name())
print(stud1.get_age())    
    


