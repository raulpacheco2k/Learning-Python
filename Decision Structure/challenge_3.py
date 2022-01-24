# Faça um programa que verifique se uma letra digitada é "F" ou "M".
# Escreva Feminino se a letra for F ou Masculino se a letra for M se nenhum dos dois escrever Sexo Inválido.

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


print(get_gender())
