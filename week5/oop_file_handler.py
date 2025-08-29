# Assignment 1: Design Your Own Class

# Base Class
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def call(self):
        print(f"{self.brand} {self.model} is making a call...")

    def details(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}")


# Derived Class (Inheritance)
class Smartwatch(Smartphone):
    def __init__(self, brand, model, price, style):
        super().__init__(brand, model, price)
        self.style = style

    def call(self):  # Polymorphism (method overriding)
        print(f"{self.brand} {self.model} Smartwatch is making a call from your wrist!")

    def details(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Style: {self.style}, Price: {self.price}")


# Activity 2: Polymorphism Challenge
class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

class Boat:
    def move(self):
        print("Sailing 🚤")


# --- Test the Classes ---
phone = Smartphone("Samsung", "Galaxy S24", 800)
watch = Smartwatch("Apple", "Watch Series 9", 500, "Sport")

phone.details()
phone.call()
watch.details()
watch.call()

print("\n--- Polymorphism in Action ---")
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()
