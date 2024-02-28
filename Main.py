class Employee:
    def __init__(self,name, age, salary, gender):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender
    def employee_details(self):
        print("name:",self.name)
        print("age:",self.age)
        print("salary:",self.salary)
        print("gender:",self.gender)
e1=Employee('Riya',22,80000,'female')
e1.employee_details()
