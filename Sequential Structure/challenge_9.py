# Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

temperature_fahrenheit = float(input('what is the temperature in degrees Fahrenheit? '))

celsius = 5 * ((temperature_fahrenheit-32) / 9)

print(f"The temperature in Celsius is {celsius:.2f}")
