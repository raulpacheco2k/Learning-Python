# Faça um programa que verifique se uma letra digitada é "F" ou "M".
# Escreva Feminino se a letra for F ou Masculino se a letra for M se nenhum dos dois escrever Sexo Inválido.

def get_gender():
    while True:
        genre = str(input('Você é homem ou mulher? Insira H para homem ou M para mulher: ')).upper()

        if genre in ('H', 'M'):
            if genre == "H":
                return "Homem"
            else:
                return "Mulher"
        else:
            print('Gênero inválido. Tente novamente.')
            continue


print(get_gender())
