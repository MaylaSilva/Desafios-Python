'''O programa deve calcular e apresentar a quantidade de números pares e
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
informar o valor zero. Certifique-se de incluir validações para garantir que
apenas números positivos sejam considerados na contagem e cálculos.
'''

listaNumeros = []

par = 0
impar = 0

print("Caso deseje finalizar, digite 0!")

while True:
    numero = int(input("Digite um número: "))
    if numero < 0:
        print("O número digitado precisa ser maior que zero!")
    elif numero == 0:
        break
    else: 
        listaNumeros.append(numero)
        

for numero in listaNumeros:
    if numero %2 == 0:
        par += 1
    else:
        impar +=1

print(f"Quantidade de números pares digitados foi {par} e a quantidade de ímpar foi {impar}")