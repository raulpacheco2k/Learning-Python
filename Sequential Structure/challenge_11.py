# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# O produto do dobro do primeiro com a metade do segundo.
# A soma do triplo do primeiro com o terceiro.
# O terceiro ao cubo.

whole_number_one = int(input('Type first whole number: '))
whole_number_two = int(input('Type second whole number: '))
real_number = float(input('Type second real number: '))

print(f"The product of double the first with half the second: {(whole_number_one * 2) * (whole_number_two / 2)}.")
print(f'The sum of triple the first with the third: {(whole_number_one * 3) + real_number}.')
print(f'The third cubed: {real_number ** 3}.')
