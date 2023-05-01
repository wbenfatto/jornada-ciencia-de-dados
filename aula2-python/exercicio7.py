# Verificar se o usuário digitou o login e a senha corretos
# usuario = miveiga
# senha = 12345!

login = input('Digite seu usuario: ')
senha = input('Digite sua senha: ')

if login == 'miveiga' and senha == '12345!':
    print('Login realizado com sucesso')
else:
    print('usuário e/ou senha incorretos')