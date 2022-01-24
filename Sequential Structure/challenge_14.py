# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar a renda diária do seu trabalho.
# Toda vez que ele traz um peso de pescado acima dos 50 quilos estabelecidos pelo regulamento de pesca do estado de
# São Paulo, ele deve pagar uma multa de $ 4,00 por quilo. João precisa que você faça um programa para calcular o excesso.

weight = float(input('João, how many kilos of fish did you catch? '))

surplus = weight - 50
fine = 4.00 * surplus

print(f"Hello João, you caught {weight}Kg of fish. This is value surplus in {surplus}Kg and you have to pay ${fine:.2f}")