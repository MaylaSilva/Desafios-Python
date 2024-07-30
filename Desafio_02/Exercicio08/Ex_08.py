'''Criar um programa em Python que solicite três números ao usuário, utilize
estruturas condicionais para determinar o maior entre eles e apresente o
resultado.'''

primeiroNumero = int(input("Digite o primeiro número: "))
segundoNumero = int(input("Digite o segundo número: "))
terceiroNumero = int(input("Digite o terceiro número: "))

if primeiroNumero > segundoNumero and primeiroNumero > terceiroNumero:
    print(f"O maior número digitado é: {primeiroNumero}")
elif segundoNumero > primeiroNumero and segundoNumero > terceiroNumero:
    print(f"O maior número digitado é: {segundoNumero}")
else:
    print(f"O maior número digitado é: {terceiroNumero}")
