# Faça um programa que calcule a área de um quadrado, então mostre ao usuário o dobro dessa área.

def double_area():
    axis_x = float(input('Insira o eixo X do quadrado:'))
    axis_y = float(input('Insira o eixo Y do quadrado:'))
    calculation = (axis_x * axis_y) * 2
    return calculation


print(f'O dobro da área de um quadrado é {double_area()}')
