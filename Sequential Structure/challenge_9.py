# Make a program that asks for the temperature in degrees Fahrenheit, transform and show the temperature in degrees Celsius.

temperature_fahrenheit = float(input('what is the temperature in degrees Fahrenheit? '))

celsius = 5 * ((temperature_fahrenheit-32) / 9)

print(f"The temperature in Celsius is {celsius:.2f}")
