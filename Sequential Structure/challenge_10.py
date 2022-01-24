# Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

temperature_celsius = float(input('what is the temperature in degrees CelsiusFahrenheit? '))

fahrenheit = (1.8 * temperature_celsius) + 32

print(f"The temperature in Celsius is {fahrenheit:.2f}")
