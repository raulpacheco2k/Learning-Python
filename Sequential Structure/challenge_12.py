# Tomando como dado de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72,7*altura) - 58

def get_height():
    while True:
        try:
            height = int(input('How tall are you in centimeters? '))
        except ValueError:
            print('Please, type a valid number.. Try again.')
        else:
            return height


height = get_height()

weight = (72.7 * (height/100)) - 58

print(f'Your ideal weight is {weight:.2f}Kg.')