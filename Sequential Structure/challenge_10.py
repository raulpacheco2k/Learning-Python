# Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

temperature_celsius = float(input('Qual a temperatura em graus Celsius?'))

fahrenheit = (1.8 * temperature_celsius) + 32

print(f"A temperatura em Fahrenheit é {fahrenheit:.2f}")
