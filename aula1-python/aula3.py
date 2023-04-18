import os
# limpar tela do terminal
os.system('cls')

nome = input('Digite o seu nome: ')
salario = input('Digite o seu salario: ')
aumento = input('Digite a % do aumento: ')

salario = float(salario)
aumento = float(aumento)

aumento = salario * aumento / 100
salario = salario + aumento

print('Olá {0}, seu aumento é de {1:.2f} e o seu novo salário é de {2:.2f}'.format(nome, aumento, salario))
