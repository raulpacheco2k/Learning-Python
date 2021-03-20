# Make a program that asks for the radius of a circle, calculate and show its area.

def circle_radius():
    circle_radius = float(input('What is circle radius in meters? '))
    area = 3.1415926535898 * (circle_radius ** 2)
    return area


print(f'The area of the circle is: {circle_radius():.2f}m².')
