class Employee:
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

    def work(self):
        pass

class Developer(Employee):
    def work(self):
        return f"{self.name} is coding in the {self.dept} department."

class Designer(Employee):
    def work(self):
        return f"{self.name} is designing in the {self.dept} department."

class Manager(Employee):
    def work(self):
        return f"{self.name} is mananing tasks in the {self.dept} department."

dev = Developer("Riya", "Software Development")
print(dev.work())   

des = Designer("Arun", "UI/UX Design")
print(des.work())  

man = Manager("Keerthi", "Project Management")
print(man.work())     
