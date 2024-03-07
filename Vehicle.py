class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage = mileage
        self.cost = cost
    def show_details(self):
        print("The mileage is",self.mileage)
        print("The cost of the vehicle is",self.cost)
Audi = Vehicle(2000,2000000)
Audi.show_details()
class Scooter(Vehicle):
    def __init__(self,mileage,cost):
        super().__init__(mileage,cost)
        print("This is a Scooty")
Scooty = Scooter(500,80000)
Scooty.show_details()

