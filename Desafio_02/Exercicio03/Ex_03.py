'''Faça um programa que peça uma nota, entre zero e dez. Mostre uma
mensagem caso o valor seja inválido e continue pedindo até que o usuário
informe um valor válido.
'''

nome = input("Qual é seu nome? ")

nota = int(input(f"Olá! {nome}. Digite sua nota de 0 à 10: "))

while nota < 0 or nota > 10:
    print("Valor Inválido")
    nota = int(input("Digite sua nota de 0 à 10! "))

print("Obrigada!")