# Tendo como entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# use as seguintes fórmulas:
# Para homem: (72,7*h) - 58
# Para mulheres: (62,1*h) - 44,7

def get_gender():
    while True:
        genre = str(input('You are male or female? Insert W or M: ')).upper()

        if genre in ('W', 'M'):
            if genre == "W":
                return "Woman"
            else:
                return "Man"
        else:
            print('Invalid Gender. Try again. ')
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

    if genre == 'Man':
        weight = (72.7 * (height / 100)) - 58
    else:
        weight = (62.1 * (height / 100)) - 44.7
    return weight


ideal_weight = calculate_ideal_weight()

print(f'Your ideal weight is {ideal_weight:.2f}Kg.')
