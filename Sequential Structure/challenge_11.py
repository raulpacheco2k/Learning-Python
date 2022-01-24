# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# O produto do dobro do primeiro com a metade do segundo.
# A soma do triplo do primeiro com o terceiro.
# O terceiro ao cubo.

whole_number_one = int(input('Digite o primeiro número inteiro:'))
whole_number_two = int(input('Digite o segundo número inteiro:'))
real_number = float(input('Digite um número real:'))

print(f"O produto do dobro do primeiro pela metade do segundo: {(whole_number_one * 2) * (whole_number_two / 2)}.")
print(f'A soma do triplo do primeiro com o terceiro: {(whole_number_one * 3) + real_number}.')
print(f'O terceiro ao cubo: {real_number ** 3}.')
