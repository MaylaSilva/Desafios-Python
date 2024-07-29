#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.Calcule e mostre o total do seu salário no referido mês.

print("Calcule quanto você receberá no mês")

horasTrabalhadas = int(input("Quantas horas você trabalhou esse mês? "))
valorHora = int(input("Qual é o valor da sua hora trabalhada? "))
salario = valorHora * horasTrabalhadas

print(f"Seu salário será de {salario:.2f} reais")