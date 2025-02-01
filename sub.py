class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"Vehicle: {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def display_info(self):
        return f"Car: {self.make} {self.model}, Doors: {self.num_doors}"
if __name__ == "__main__":
    print("\nVehicles\n")
    vehicle = Vehicle("Honda", "Click 125cc")
    print(vehicle.display_info())  
    vehicle = Vehicle("Honda", "XRM 125cc")
    print(vehicle.display_info())  
    vehicle = Vehicle("Yamaha", "Mio i 125cc")
    print(vehicle.display_info())  
    vehicle = Vehicle("Yamaha", "Sniper 155cc")
    print(vehicle.display_info())  
    vehicle = Vehicle("Suzuki", "Raider 150cc")
    print(vehicle.display_info()) 

    print("\nCars\n")
    car = Car("Toyota", "Supra", 2)
    print(car.display_info())  
    car = Car("Honda", "Civic", 4)
    print(car.display_info()) 
    car = Car("Lamborghini", "Huracan", 2)
    print(car.display_info()) 
    car = Car("Mitsubishi", "Lancer", 4)
    print(car.display_info()) 
    car = Car("Toyota", "Tamaraw", 5)
    print(car.display_info()) 


