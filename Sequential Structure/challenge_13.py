# Having as input the height (h) of a person, build an algorithm that calculates your ideal weight,
# use the following formulas:
# For man: (72.7*h) - 58
# For women: (62.1*h) - 44.7

def get_gender():
    while True:
        genre = str(input('You are male or female? Insert M or F: ')).upper()

        if genre in ('M', 'F'):
            return genre
        else:
            print('Unidentified gender. Try again. ')
            continue


def get_height():
    while True:
        try:
            height = int(input('How tall are you in centimeters? '))
        except ValueError:
            print("Invalid value. Please, type your height in centimeters.")
            continue
        else:
            return height


def calculate_ideal_weight():
    genre = get_gender()
    height = get_height()

    if genre == 'M':
        weight = (72.7 * (height / 100)) - 58
    else:
        weight = (62.1 * (height / 100)) - 58
    return weight


ideal_weight = calculate_ideal_weight()

print(f'Your ideal weight is {ideal_weight:.2f}Kg.')
