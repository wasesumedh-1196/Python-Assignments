# Create a module with functions to calculate the area of a circle (with radius),
# rectangle (with length and width) and triangle (with length and width).
# Based on user input, determine and show the area of shapes using the user-defined module.

import math

def circle_area(radius):
    return math.pi * radius * radius

def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height


print("1. Area of Circle")
print("2. Area of Rectangle")
print("3. Area of Triangle")

choice = int(input("Enter your choice: "))

if choice == 1:
    r = float(input("Enter radius: "))
    print("Area of Circle:", circle_area(r))

elif choice == 2:
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print("Area of Rectangle:", rectangle_area(l, w))

elif choice == 3:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    print("Area of Triangle:", triangle_area(b, h))

else:
    print("Invalid choice")

