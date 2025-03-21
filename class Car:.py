class Car:
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    # Method to start the car
    def start(self):
        print("Car Started.")

    # Method to accelerate the car
    def accelerate(self, mph):
        self.speed += mph
        print(f"Accelerating. Current speed: {self.speed} mph")

    # Method to brake the car
    def brake(self, brake_speed):
        self.speed -= brake_speed
        if self.speed < 0:
            self.speed = 0
        print(f"Braking. Current speed: {self.speed} mph")

    # Method to display car information
    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Speed: {self.speed} mph")


# Create instances (objects) of the Car class
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Tesla", "Model 3", 2023)

# Use the methods of the objects
car1.start()
car1.accelerate(35)
car1.brake(20)

# Display info about cars
car1.display_info()
car2.display_info()
