# Faça um programa que peça as 4 notas bimestrais e mostre a média.

notes = []

print('Cálculo médio bimestral!')

for i in range(1, 5):
    note = int(input(f'Inserir uma nota: '))
    notes.append(note)

print(f"Sua média bimestral é: {sum(notes)/4}.")
