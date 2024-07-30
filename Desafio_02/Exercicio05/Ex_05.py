'''Desenvolva um programa que solicite ao usuário os comprimentos dos três
lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
equilátero: todos os lados com o mesmo valor
isósceles: dois lados com o mesmo valor
escaleno: todos os lados com medidas distintas.'''

print("Vamos descobrir qual é o tipo de triângulo?")

triangulo1 = int(input("Digite o tamanho do primeiro lado: "))
triangulo2 = int(input("Digite o tamanho do segundo lado: "))
triangulo3 = int(input("Digite o tamanho do terceiro lado: "))


if triangulo1 == triangulo2 == triangulo3:
    print("Triângulo Equilátero")
elif triangulo1 == triangulo2 or triangulo1 == triangulo3 or triangulo2 == triangulo3:
    print ("Triângulo Isósceles")
else:
    print("Triângulo Escaleno")