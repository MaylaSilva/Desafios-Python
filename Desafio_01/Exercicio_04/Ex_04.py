#Receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida. Calcule e imprima o consumo médio em km/l.

print("Cálculo de consumo de combustível")
combustivel = float(input("Digite quantos litros de combustível foram consumidos: "))
distancia = float(input("Digite a distância percorrida em quilômetros: "))
consumo = distancia/combustivel

print(f"O consumo foi de aproximadamente {consumo:.2f}km/l")