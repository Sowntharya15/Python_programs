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
    def __init__(self,mileage,cost,brand):
        super().__init__(mileage,cost)    # over riding init method
        self.brand = brand 
    def show_scooter_details(self):
        print("This is a Scooty")
        print("The brand is",self.brand)
     
Scooty = Scooter(500,80000,"Vespa")
Scooty.show_details()
Scooty.show_scooter_details()