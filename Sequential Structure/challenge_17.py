# Make a Program for a paint store. The program should ask for the size in square meters of the area to be painted.
# Consider that the coverage of the paint is 1 liter for every 6 square meters and that the paint is sold in cans
# of 18 liters, which cost R$ 80.00 or in gallons of 3.6 liters, which cost R$ 25.00.
# Tell the user the quantities of paint to be purchased and the respective prices.
# Round the values up, that is, consider full cans.

def get_float_number(parameter):
    while True:
        try:
            float_number = float(input(parameter))
        except ValueError:
            print("This value is not valid, please type a number.")
        else:
            return float_number


area = get_float_number("How many square meters will be painted? ")
liters_required = area / 6
can_of_paint = 0
paint_gallon = 0

while True:
    if liters_required >= 18:
        liters_required -= 18
        can_of_paint += 1
    else:
        liters_required -= 3.6
        paint_gallon += 1
        if liters_required < 0:
            break

price = (can_of_paint * 80) + (paint_gallon * 25)
print(f"You will need {can_of_paint} can of paint and {paint_gallon} gallons of paint, it will cost ${price}.")
