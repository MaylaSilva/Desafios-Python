'''Escreva um programa que calcule o salário líquido. Lembrando de
declarar o salário bruto e o percentual de desconto do Imposto de
Renda.
● Renda até R$ 1.903,98: isento de imposto de renda;
● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%'''

print("Vamos ver quanto é seu salário líquido")
salario = float(input("Digite seu salário: "))

if salario <= 1903.98: 
    print("Seu não tem desconto de imposto de renda!")
elif salario > 1903.98 and salario <= 2826.65: 
    imposto = salario * 0.075
    print("Você tem um desconto de 7,5% de imposto de renda")
elif salario > 2826.65 and salario <= 3751.05: 
    imposto = salario * 0.15
    print("Você tem um desconto de 15% de imposto de renda")
elif salario > 3751.05 and salario <= 4664.68: 
    imposto = salario * 0.225
    print("Você tem um desconto de 22,5% de imposto de renda")
else:
    imposto = salario * 0.275
    print("Você tem um desconto de 27,5% de imposto de renda")

desconto = salario - imposto
print(f"Seu salário líquido ficará: {desconto:.2f}")