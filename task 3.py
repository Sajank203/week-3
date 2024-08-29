class Vehicle:
def __init__(self, make, model):
self.make = make
self.model = model
def get_info(self):
return f"{self.make} {self.model}"
class Car(Vehicle):
def start_engine(self):
return "Engine started"
car = Car("Toyota", "Corolla")
print(car.get_info())
print(car.start_engine())