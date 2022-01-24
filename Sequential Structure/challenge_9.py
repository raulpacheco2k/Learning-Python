# Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

temperature_fahrenheit = float(input('Qual é a temperatura em graus Fahrenheit?'))

celsius = 5 * ((temperature_fahrenheit-32) / 9)

print(f"A temperatura em Celsius é {celsius:.2f}")
