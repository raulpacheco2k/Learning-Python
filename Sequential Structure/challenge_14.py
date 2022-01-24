# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar a renda diária do seu trabalho. Toda
# vez que ele traz um peso de pescado acima dos 50 quilos estabelecidos pelo regulamento de pesca do estado de São
# Paulo, ele deve pagar uma multa de R$ 4,00 por quilo. João precisa que você faça um programa para calcular o excesso.

weight = float(input('João, quantos quilos de peixe você pescou? '))

surplus = weight - 50

if weight == 0:
    print("Você não pescou nada!")
elif surplus > 0:
    fine = 4.00 * surplus
    print(f"Olá João, você pegou {weight}Kg de peixes. Este é o excedente de valor em {surplus:.2f}Kg e você tem que pagar R$ {fine:.2f} em multa!")
else:
    print(f"Olá João, você pegou {weight}Kg de peixes. Você não precisará pagar multa!")
