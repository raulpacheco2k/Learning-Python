# Make a program that converts meters to centimeters.

notes = []

print('Converting meters to centimeters!')

while True:
    try:
        meters = float(input('Meters: '))
        break
    except ValueError:
        print('Please, insert a number.')

print(f"{meters} meters is {meters*100} centimeters.")
