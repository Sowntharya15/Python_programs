class Employee:
    def __init__(self, name, salary, department):
        self._name = name
        self._salary = salary
        self._department = department

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def get_salary(self):
        return self._salary

    def set_salary(self, new_salary):
        self._salary = new_salary

    def get_department(self):
        return self._department

    def set_department(self, new_department):
        self._department = new_department

e1 = Employee("John", 50000, "Engineering")

print("Employee Details:")
print("Name:", e1.get_name())
print("Salary:", e1.get_salary())
print("Department:", e1.get_department())


e1.set_salary(45000)
e1.set_department("Marketing")
print()
print("Updated Employee Details:")
print("Name:", e1.get_name())
print("Salary:", e1.get_salary())
print("Department:", e1.get_department())
