# Tomando como dado de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72,7*altura) - 58

def get_height():
    while True:
        try:
            height = int(input('Qual a sua altura em centímetros?'))
        except ValueError:
            print('Por favor, digite um número válido. Tente novamente.')
        else:
            return height


height = get_height()

weight = (72.7 * (height/100)) - 58

print(f'Seu peso ideal é {weight:.2f}Kg.')