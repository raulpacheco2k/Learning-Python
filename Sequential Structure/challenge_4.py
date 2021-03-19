# Make a program that asks for the 4 bimonthly notes and shows the average.

notes = []

print('Bimonthly average calculation!')

for i in range(1, 5):
    note = int(input(f'Insert: '))
    notes.append(note)

print(f"Your bimonthly average is {sum(notes)/4}.")
