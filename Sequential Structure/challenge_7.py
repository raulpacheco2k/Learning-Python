# Make a program that calculates the area of a square, then show the user double that area

def double_area():
    axis_x = float(input('Insert a X axis of the square: '))
    axis_y = float(input('Insert a Y axis of the square: '))
    calculation = (axis_x * axis_y) * 2
    return calculation


print(f'The double of area of a square is {double_area()}')
