class Vehicle:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed

    def show_details(self):
        print("Brand:", self.brand)
        print("Max Speed:", self.max_speed, "km/h")

class Car(Vehicle):

    def __init__(self, model, brand, max_speed):
        self.model = model
        self.seats = self.seats
        super().show_details()

    def show_details(self):
        print("Model:", self.model)
        print("Seats:", self.seats)
        super().__init__(brand, self.max_speed)

    def fuel_type(self, fuel):
        print(self.model, "uses", fuel)

my_car = Car("City Rider", 5, "F1 Car", 220)


my_car.show_details()
my_car.fuel_type("petrol")


print("Is Car a subclass of Vehicle?", issubclass(Car, Vehicle))
