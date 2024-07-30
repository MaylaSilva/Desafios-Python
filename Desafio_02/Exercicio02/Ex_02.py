'''Faça um Programa que pergunte em que turno você estuda. Peça para
digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom
Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso'''

nome = input("Qual é seu nome? ")

print(f"Olá! {nome}. Qual é o período que você estuda?")

periodo = input("Digite M para Matutino, V para Vespertino ou N para Noturno! ").upper()

while periodo != "M" and periodo != "V" and periodo != "N":
    print("Valor Inválido")
    periodo = input("Digite M para Matutino, V para Vespertino ou N para Noturno! ").upper()

if periodo == "M":
    print(f"Tenha um bom dia {nome}!")
elif periodo == "V":
    print(f"Tenha uma boa tarde {nome}!")
else:
    print(f"Tenha uma boa noite {nome}!")