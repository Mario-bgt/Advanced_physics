#!/usr/bin/env python3

# The purpose of this file is illustrating the class usages. This script
# is irrelevant for the grading and you can freely change its contents.

from cone import Cone
from cube import Cube
from cylinder import Cylinder

# Create first cone object
cone_1 = Cone(2, 4, 2, "red", True)

# Create another cone object
cone_2 = Cone(5.64, 4.2, 8.7, "black", False)

# Create a cube object
cube = Cube(7.2, "white", True)
print(f"Color of the cube object is: {cube.color}")

# Update cube color
cube.color = "yellow"

# See if the color of cube object is changed
print(f"Color of the cube object is: {cube.color}")

# See the area and volume of the cone_1
print(f"cone_1 area is: {cone_1.area()} cone_2 volume is: {cone_1.volume()}")

cylinder_1 = Cylinder(2, 4, "red", True)

cylinder_2 = Cylinder(5.64, 4.2, "black", False)

print(f"cylinder_1 area is: {cylinder_1.area()} cylinder_2 volume is: {cylinder_1.volume()}")
