'''Escreva um programa que calcule o tempo de uma viagem. Faça um
comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
● avião = 600 km/h
● carro = 100 km/h
● ônibus = 80 km/h'''

print ("Calculadora de tempo médio de viagem")

distancia = int(input("Digite a distância que irá percorrer em quilômetros: "))
velocidade = int(input("Digite a velocidade média a ser feita: "))
tempo =  distancia/velocidade
onibus = distancia/80
carro = distancia/100
aviao = distancia/600

print(f"O tempo médio gasto considerando sua média de velocidade é de {tempo} horas, se for considerar o tempo de carro é de aproximadamente {carro} horas, de ônibus é de {onibus} horas e de avião é de {aviao} horas")