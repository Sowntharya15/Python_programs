class Parent():
    def assign_name(self,name):
        self.name = name
    def show_name(self):
        print(self.name)

class Child(Parent):
    def assign_age(self,age):
        self.age = age 
    def show_age(self):
        print(self.age)

class Grandchild(Child):
    def assign_salary(self,salary):
        self.salary = salary
    def show_salary(self):
        print(self.salary)

g1=Grandchild()
g1.assign_name("Name : SOWNTHARYA")
g1.assign_age("Age : 20")
g1.assign_salary("Salary : 500000")
g1.show_name()
g1.show_age()
g1.show_salary()

