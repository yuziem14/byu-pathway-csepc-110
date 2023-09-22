import math

# PI_VALUE = 3.14 (replaced by math.pi constant)

# Constant to convert square centimeters to square meters
CONVERT_SQUARE_METERS = 1 / 10000

# Sphere constant used in the formula (V = 4/3 * PI * r³)
SPHERE_CONSTANT = 4 / 3

# Core Requirement: Square Area
square_side = float(input('What is the length of a side of the square (in centimeters)? '))
square_area = square_side ** 2
print(f'The area of the square is: {square_area} cm² or {square_area * CONVERT_SQUARE_METERS} m²')

# Core Requirement: Rectangle Area
rectangle_length = float(input('What is the length of rectangle (in centimeters)? '))
rectangle_width = float(input('What is the width of rectangle (in centimeters)? '))
rectangle_area = rectangle_length * rectangle_width
print(f'The area of the rectangle is: {rectangle_area} cm² or {rectangle_area * CONVERT_SQUARE_METERS:.4f} m²')

# Core Requirement: Circle Area
circle_radius = float(input('What is the radius of the circle (in centimeters)? '))
circle_area = math.pi * (circle_radius ** 2)
print(f'The area of the circle is: {circle_area:.4f} cm² or {circle_area * CONVERT_SQUARE_METERS:.6f} m²')

'''
Stretch Challenge

Prompt the user for a single length value, then compute and display the areas of a square with that length of side, a circle with that radius, and then the volumes of a cube with that side and a sphere with that radius, all from the same value from the user.
'''

print()
length_value = float(input('What is the length/radius? '))

# Square Area
square_area = length_value ** 2
print(f'The area of the square is: {square_area}')

# Circle Area
circle_area = math.pi * (length_value ** 2)
print(f'The area of the circle is: {circle_area:.4f}')

# Cube Volume
cube_volume = length_value ** 3
print(f'The volume of the cube is: {cube_volume}')

# Sphere Volume
sphere_volume = SPHERE_CONSTANT * math.pi * (length_value ** 3)
print(f'The volume of the sphere is: {sphere_volume:.4f}')
