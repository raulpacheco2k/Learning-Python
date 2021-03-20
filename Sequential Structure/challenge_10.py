# Make a program that asks for the temperature in degrees Celsius, transform it and show it in degrees Fahrenheit.

temperature_celsius = float(input('what is the temperature in degrees CelsiusFahrenheit? '))

fahrenheit = (1.8 * temperature_celsius) + 32

print(f"The temperature in Celsius is {fahrenheit:.2f}")
