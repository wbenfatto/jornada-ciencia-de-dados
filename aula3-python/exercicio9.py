#Faça um programa que solicite ao usuário uma senha. 
#O usuário tem três tentativas para digitar a senha correta. 
#O programa deve exibir uma mensagem de erro caso a senha esteja incorreta 
#e uma mensagem de sucesso caso a senha esteja correta ou o usuário 
# tenha esgotado as tentativas.

contador = 0

while contador < 3:
    senha = input('Digite a senha: ')
    if senha != '12345!':
        print('Senha incorreta')
        contador += 1
    else:
        print('Logado')
        break
    if contador == 3:
        print('Excedeu o limite de 3 tentativas')
        break