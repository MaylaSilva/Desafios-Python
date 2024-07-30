'''Crie um programa que solicite ao usuário um login e uma senha. O
programa deve permitir o acesso apenas se o usuário for "admin" e a senha
for "admin123", caso contrário imprima uma mensagem de erro.
'''

tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    login = input("Digite seu login: ")
    password = input("Digite sua senha: ")
    
    if login == "admin" and password == "admin123":
        print("Bem-vindo(a)")
        break
    else:
        tentativas += 1
        print("Login ou Senha incorreta!")
        
    if tentativas == max_tentativas:
        print("Conta bloqueada após três tentativas incorretas.")