# Faça um programa para uma loja de tintas. O programa deve solicitar o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18
# litro, que custam R$ 80,00. Informe ao usuário as quantidades de latas de tinta a serem compradas e o preço total.


def get_float_number(parameter):
    while True:
        try:
            float_number = float(input(parameter))
        except ValueError:
            print("This value is not valid, please type a number.")
        else:
            return float_number


area = get_float_number("How many square meters will be painted? ")
liters_required = area / 3
can_of_paint = round(liters_required / 18)
preco = can_of_paint * 80

print(f"You will need {can_of_paint} can of paint")
print(f"It will cost ${preco}.")
