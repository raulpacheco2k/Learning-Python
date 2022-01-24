# Faça um programa que peça o raio de um círculo, calcule e mostre sua área.

def circle_radius():
    circle_radius = float(input('O que é o raio do círculo em metros?'))
    area = 3.1415926535898 * (circle_radius ** 2)
    return area


print(f'A área do círculo é: {circle_radius():.2f}m².')
