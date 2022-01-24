# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas.
# Calcule e mostre seu salário total do mês.

hourly_wage = float(input('What is your hourly wage? '))
hours_worked = float(input('How many hours did you work? '))

salary = hours_worked * hourly_wage

print(f" Your salary is ${salary}")
