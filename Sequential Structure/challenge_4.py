# Faça um programa que peça as 4 notas bimestrais e mostre a média.

notes = []

print('Bimonthly average calculation!')

for i in range(1, 5):
    note = int(input(f'Insert: '))
    notes.append(note)

print(f"Your bimonthly average is {sum(notes)/4}.")
