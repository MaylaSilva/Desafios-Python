from datetime import datetime

#Peça ao usuário para informar o ano de nascimento. Em seguida, calcule e imprima a idade atual.

print("Vamos descobrir sua idade?")
anoNascimento = int(input("Digite seu ano de nascimento: "))
anoAtual = datetime.now().year
idade = anoAtual-anoNascimento

print (f"Sua idade é de {idade} anos!")