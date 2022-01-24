# Faça um programa que verifique se uma letra digitada é "F" ou "M".
# Escreva Feminino se a letra for F ou Masculino se a letra for M se nenhum dos dois escrever Sexo Inválido.

def vowel_or_consonant():
    while True:
        letter = str(input("Digite uma letra: ")).upper()

        if validates_if_it_is_a_letter(letter):
            if letter in ("A", "E", "I", "O", "U"):
                print("A letra é uma vogal.")
            else:
                print("A letra é uma consoante.")
            break
        else:
            continue


def validates_if_it_is_a_letter(letter):
    if len(letter) > 1:
        print("Digite somente uma letra")
    elif letter in "1234567890":
        print("Digite uma letra.")
    else:
        return True


vowel_or_consonant()