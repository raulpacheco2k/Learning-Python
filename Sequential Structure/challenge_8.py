# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas.
# Calcule e mostre seu salário total do mês.

hourly_wage = float(input('Qual é o seu salário por hora? '))
hours_worked = float(input('Quantas horas você trabalhou? '))

salary = hours_worked * hourly_wage

print(f"Você deve receber R$ {salary}")
