
# Create A base class Vehicle with methode move(), and two subclasses Car 
# and Bicycle that override the move() method. in both subclasses.
# The cards should print "Driving on the road" and the bicycle should print "riding on the road."
# Demonstrate polymorphism by calling the move() method on both objects.

# Base class
class Vehicle:
    def move(self):
        print("Vehicle is moving")

# Subclass : Car
class Car(Vehicle):
    def move(self):
        print("Driving on the road")

# Subclass : Bicycle
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the road")

# Create objects
car = Car()
bicycle = Bicycle()

# Put objects in a list
vehicles = [car, bicycle]

# Use loop (Polymorphism)
for v in vehicles:
    v.move()
