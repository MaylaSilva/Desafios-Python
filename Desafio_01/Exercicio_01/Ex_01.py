#Faça um Programa que peça dois números, realize as principais operações soma, subtração, multiplicação, divisão

print("Bem-vindo a calculadora!")
primeiroNumero = float(input("Digite o primeiro número: "))
segundoNumero = float(input("Digite o primeiro número: "))
soma = primeiroNumero + segundoNumero
subtracao = primeiroNumero - segundoNumero
multiplicacao = primeiroNumero * segundoNumero
divisao = primeiroNumero / segundoNumero

print(f"O resultado de cada operação é: \nSoma: {soma:.2f} \nSubtração: {subtracao:.2f}\nMultiplicação: {multiplicacao:.2f}\nDivisão: {divisao:.2f}")