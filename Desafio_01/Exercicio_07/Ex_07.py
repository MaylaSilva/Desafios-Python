'''Solicite ao usuário o peso em kg e a altura em metros. Calcule e
imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso / (altura x altura).'''

print("Calculadora de IMC")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura, em metros (exemplo: 1.6): "))
imc=peso/(altura*altura)

print(f"Seu IMC é de {imc:.2f}")