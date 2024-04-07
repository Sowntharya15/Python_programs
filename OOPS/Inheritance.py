class Organism:
    def __init__(self,name):
        self.name = name

class Plant(Organism):
    def photosynthesize(self):
        print(f"{self.name} is performing photosynthesis.")

class Animal(Organism):
    def move(self):
        print(f"{self.name} is moving.")

rose = Plant("Rose")
rose.photosynthesize()  

tiger = Animal("Tiger")
tiger.move()  

print()

# Multilevel Inheritance :

class Organism:
    def __init__(self, name):
        self.name = name

class LivingThing:
    def grow(self):
        print(f"{self.name} is growing.")

class Plant(Organism, LivingThing):
    def photosynthesize(self):
        print(f"{self.name} is performing photosynthesis.")

class Animal(Organism, LivingThing):
    def move(self):
        print(f"{self.name} is moving.")

rose = Plant("Rose")
rose.grow()  
rose.photosynthesize()  

tiger = Animal("Tiger")
tiger.grow()  
tiger.move()  
