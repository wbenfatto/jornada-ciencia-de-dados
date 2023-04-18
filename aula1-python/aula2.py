import os
# limpar tela do terminal
os.system('cls')

nome = input('Digite o nome: ')
idade = input('Digite a idade: ')

idade = int(idade)

print('Nome:', nome)
print('Idade:', idade)

print(type(nome))
print(type(idade))

dias = idade * 365
print('Você já viveu:', dias, 'dias')