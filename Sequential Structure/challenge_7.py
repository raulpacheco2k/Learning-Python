# Faça um programa que calcule a área de um quadrado, então mostre ao usuário o dobro dessa área.

def double_area():
    axis_x = float(input('Insert a X axis of the square: '))
    axis_y = float(input('Insert a Y axis of the square: '))
    calculation = (axis_x * axis_y) * 2
    return calculation


print(f'The double of area of a square is {double_area()}')
