# Faça um programa que peça o nome do usuário e verifique se ele é 'admin'
# Ele é admin se for Lucas ou Pedro.

usuario = input('Nome do usuário: ').upper()

if usuario == 'LUCAS' or usuario == 'PEDRO':
    print(f'Bem Vindo {usuario}')
else:
    print('Não autorizado')

