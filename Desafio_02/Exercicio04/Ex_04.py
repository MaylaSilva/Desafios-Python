'''Implemente um programa que classifique um aluno com base em sua
pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se
a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é
reprovado'''

nome = input("Qual é seu nome? ")

nota = int(input(f"Olá! {nome}. Digite sua nota de 0 à 10: "))

while nota < 0 or nota > 10:
    print("Valor Inválido")
    nota = int(input("Digite sua nota de 0 à 10! "))

if nota >= 7:
    print("Parabéns, você foi aprovado(a)!")
else:
    print("Reprovado(a).")