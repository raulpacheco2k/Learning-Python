# Taking as input data the height of a person, build an algorithm that calculates your ideal weight, using the following formula: (72.7*altura) - 58

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