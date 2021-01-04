import math

square_length = int(input('What is the length of a side of the square in centimeters? '))
print('The area of the square is: ' + str(square_length**2) + ' centimeters or ' + str((square_length/100)**2) + ' meters')
print('The area of the cube is: ' + str(square_length**3) + ' centimeters or ' + str((square_length/100)**3) + ' meters')

rectangle_length = int(input('What is the length of the rectangle in centimeters? '))
rectangle_width = int(input('What is the width of the rectangle in centimeters? '))
print('The area of the rectangle is: ' + str(rectangle_length * rectangle_width) + ' centimeters or ' + str((rectangle_length/100) * (rectangle_width/100)) + ' meters')

radius = int(input('What is the radius of the circle in centimeters? '))
print('The area of the circle is: ' + str(math.pi * radius**2) + ' centimeters or ' + str(math.pi * (radius/100)**2) + ' meters')
print('The area of the sphere is: ' + str(4 * math.pi * radius**2) + ' centimeters or ' + str(4 * math.pi * (radius/100)**2) + ' meters')