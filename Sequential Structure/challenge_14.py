# João Papo-de-Pescador, a good man, bought a microcomputer to control the daily income from his work. Every time he
# brings in a weight of fish above the 50 kilos established by the fishing regulations of the state of São Paulo,
# he must pay a fine of $4.00 per kilo. João needs you to make a program to calculate the excess.

weight = float(input('João, how many kilos of fish did you catch? '))

surplus = weight - 50
fine = 4.00 * surplus

print(f"Hello João, you caught {weight}Kg of fish. This is value surplus in {surplus}Kg and you have to pay ${fine:.2f}")