#Faça um Programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros.

print("Cálculo de medidas")
quilometros = int(input("Digite quantos quilômetros deseja converter: "))
metros = quilometros * 1000
centimentros = metros * 100
milimetros = centimentros * 10

print (f"{quilometros}Km são: {metros} metros, {centimentros} centimetros e {milimetros} milimetros")