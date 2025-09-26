# Object Oriented Programming (OOP): Helps us model real-world entities as classes and objects

# Example Create your own class
# Defining a class
class Car:
    # Class attributes
    color = "red"
    model = "Toyota"
    year = 2020

    def drive(self):  # Method to simulate driving
        # Simulate the car driving
        print("The car is driving")

# Creating an object
my_car = Car()
# Accessing attributes
print(my_car.color)
print(my_car.model)
print(my_car.year)
# Calling the drive method
my_car.drive()

# Constructors: the __init__ method and instance variables
# A constructor is a special method used to initialize objects.
# It is called when an object is created from a class. It allows
# each object to start with specific values. Its like building a pizza
# with different toppings for each order.

# Instance Variables are specific to each object and can vary across objects.
# For example, two Car objects can have different colors models, and speeds.

# Example: Setting up your constructor and instance variables
# def __init__ helps to initialize the object's attributes
class Car:
    def __init__(self, color, model, year):
        # Instance Variables
        self.color = color
        self.model = model
        self.year = year

    def drive(self):
        print("The car is driving")

# Creating objects with different attributes
my_car = Car("red", "Toyota", 2020)
your_car = Car("blue", "Honda", 2019)

# Accessing attributes
print(my_car.color)
print(my_car.model)
print(my_car.year)
my_car.drive()

# Accessing attributes of your_car
print(your_car.color)
print(your_car.model)
print(your_car.year)
your_car.drive()

# OOP Principles: Encapsulation, Inheritance, Polymorphism
# Inheritance: Allows a class to inherit attributes and methods from another class.
# This promotes code reusability and establishes a relationship between classes.
# Example: Imagine a Vehicle class with general features (like wheels). We can
# create subclasses like Car and Truck that inherit from Vehicle features.
class Vehicle:
    def __init__(self, wheels): # Constructor for Vehicle class
        # Instance Variable
        self.wheels = wheels

    def drive(self): # Method to simulate driving
        # Simulate the vehicle driving
        print("The vehicle is driving")

class Car(Vehicle): # Subclass of Vehicle
    def __init__(self, color, model, year): # Constructor for Car class
        # Call the constructor of the Vehicle class
        super().__init__(wheels=4)
        # Instance Variables
        self.color = color
        self.model = model
        self.year = year

class Truck(Vehicle): # Subclass of Vehicle
    def __init__(self, cargo_capacity): # Constructor for Truck class
        # Call the constructor of the Vehicle class
        super().__init__(wheels=6)
        # Instance Variables
        self.cargo_capacity = cargo_capacity
        self.load = 0

# Creating objects
car = Car("red", "Toyota", 2020)
truck = Truck(10000)

print(car.wheels) # Inherited attribute
print(truck.wheels) # Inherited attribute

# Polymorphism: The ability to present the same interface for different 
# underlying forms (data types). In our case, both Car and Truck can be driven, 
# but they may have different implementations.
def drive_vehicle(vehicle): # Polymorphic function
    # Call the drive method of the vehicle
    vehicle.drive()

# Polymorphic behavior
drive_vehicle(car)
drive_vehicle(truck)
print(truck.cargo_capacity) # Accessing Truck-specific attribute

# Another example
class Dog: # Dog class
    def speak(self): # Dog-specific implementation
        return "Woof!" # Dog sound

class Cat:
    def speak(self):
        return "Meow!"

# Polymorphic behavior
def animal_sound(animal): # Polymorphic function
    # Call the speak method of the animal
    print(animal.speak())

dog = Dog() # Dog object
cat = Cat() # Cat object

animal_sound(dog) # Dog sound
animal_sound(cat) # Cat sound

# Encapsulation: Bundling data (attributes) and methods (functions) that operate 
# on the data into a single unit (class). This restricts direct access to some 
# of the object's components, which can prevent the accidental modification of data. 
# The practice of keeping attributes and methods private to prevent unwanted
# access from outside the class.

class SecretStash:
    def __init__(self):
        self.__chocolate = 20 # Private attribute

    def take_chocolate(self, amount):
        if self.__chocolate > 9:
            self.__chocolate -= amount # Decrease the chocolate count
            print(f"You took {amount} chocolates. {self.__chocolate} left.") # Chocolate taken
        else:
            print("Not enough chocolate left!")

stash = SecretStash() # Create an instance of SecretStash
stash.take_chocolate(5) # You took 5 chocolates. 15 left.

# In summary, OOP allows you to organize code in a way that's fun, reusable, and
# efficient. By using classes and objects, you can model real-world entities,
# encapsulate data, and implement behaviors in a structured manner. This not only
# makes your code more manageable but also enhances collaboration and scalability
# in software development.
