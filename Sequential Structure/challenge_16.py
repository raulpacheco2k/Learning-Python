# Make a program for a paint store. The program should ask for the size in square meters of the area to be painted.
# Consider that the coverage of the paint is 1 liter for every 3 square meters and that the paint is sold in 18
# liter cans, which cost R$ 80,00. Tell the user the quantities of cans of paint to be purchased and the total price.


def get_float_number(parameter):
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
