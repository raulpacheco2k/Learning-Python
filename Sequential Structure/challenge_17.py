# Faça um programa para uma loja de tintas. O programa deve solicitar o tamanho em metros quadrados da área a ser
# pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
# latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as
# quantidades de tinta a serem adquiridas e os respectivos preços. Arredonde os valores para cima, ou seja,
# considere latas cheias.

def get_float_number(parameter):
    while True:
        try:
            float_number = float(input(parameter))
        except ValueError:
            print("This value is not valid, please type a number.")
        else:
            return float_number


area = get_float_number("How many square meters will be painted? ")
liters_required = area / 6
can_of_paint = 0
paint_gallon = 0

while True:
    if liters_required >= 18:
        liters_required -= 18
        can_of_paint += 1
    else:
        liters_required -= 3.6
        paint_gallon += 1
        if liters_required < 0:
            break

price = (can_of_paint * 80) + (paint_gallon * 25)
print(f"You will need {can_of_paint} can of paint and {paint_gallon} gallons of paint, it will cost ${price}.")
