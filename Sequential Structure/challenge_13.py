# Tendo como entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# use as seguintes fórmulas:
# Para homem: (72,7 * altura) - 58
# Para mulheres: (62,1 * altura ) - 44,7

def get_gender():
    while True:
        genre = str(input('Você é homem ou mulher? Insira H para homem e M para mulher: ')).upper()

        if genre in ('M', 'H'):
            if genre == "M":
                return "Mulher"
            else:
                return "Homem"
        else:
            print('Sexo inválido. Tente novamente.')
            continue


def get_height():
    while True:
        try:
            height = int(input('Qual a sua altura em centímetros? '))
        except ValueError:
            print("Valor inválido. Por favor, digite sua altura em centímetros. ")
            continue
        else:
            return height


def calculate_ideal_weight():
    genre = get_gender()
    height = get_height()

    if genre == 'Homem':
        weight = (72.7 * (height / 100)) - 58
    else:
        weight = (62.1 * (height / 100)) - 44.7
    return weight


ideal_weight = calculate_ideal_weight()

print(f'Seu peso ideal é {ideal_weight:.2f}Kg.')
