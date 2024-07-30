#Faça um programa que lê três números inteiros e os mostra em ordem crescente.

primeiroNumero = int(input("Digite o primeiro número: "))
segundoNumero = int(input("Digite o segundo número: "))
terceiroNumero = int(input("Digite o terceiro número: "))


numeros=[primeiroNumero,segundoNumero,terceiroNumero]
numeros.sort(reverse=True)

print(f"A ordem decrescente é: {numeros[0]}, {numeros[1]} e {numeros[2]}")
