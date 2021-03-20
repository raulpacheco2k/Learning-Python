# Make a program that asks how much you earn per hour and the number of hours worked.
# Calculate and show your total salary for the month.

hourly_wage = float(input('What is your hourly wage? '))
hours_worked = float(input('How many hours did you work? '))

salary = hours_worked * hourly_wage

print(f" Your salary is ${salary}")
