# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
# total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
# 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

def discount_income_tax(salary):
    IR = 11
    discount = salary - (salary * (1 - (IR/100)))
    return discount


def discount_inss(salary):
    INSS = 8
    discount = salary - (salary * (1 - (INSS/100)))
    return discount


def discount_syncidate(salary):
    SYNDICATE = 5
    discount = salary - (salary * (1 - (SYNDICATE/100)))
    return discount


hourly_wage = float(input('What is your hourly wage? '))
hours_worked = float(input('How many hours did you work? '))

salary = hours_worked * hourly_wage

print(f"Seu salário bruto é ${salary}")
print("Aplicando os descontos da folha de pagamento...")

print(f"${salary} - ${discount_income_tax(salary):.2f} = ${salary - discount_income_tax(salary):.2f}")
salary = salary - discount_income_tax(salary)
print(f"${salary} - ${discount_inss(salary):.2f} = ${salary - discount_inss(salary):.2f} ")
salary = salary - discount_inss(salary)
print(f"${salary} - ${discount_syncidate(salary):.2f} = ${salary - discount_syncidate(salary):.2f}")
salary = salary - discount_syncidate(salary)

print(f"Your net salary is: {salary:.2f}")


