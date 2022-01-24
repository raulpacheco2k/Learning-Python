# Faça um programa que converta metros em centímetros.

notes = []

print('Convertendo metros para centímetros!')

while True:
    try:
        meters = float(input('Metros: '))
        break
    except ValueError:
        print('Por favor, insira um número.')

print(f"{meters} metros é {meters*100} centímetros.")
