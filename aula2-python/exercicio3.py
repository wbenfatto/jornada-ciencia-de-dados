# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime;
# As perguntas são: 
# Telefonou para a vítima? 
# Esteve no local do crime?
# Mora perto da vitima?
# Devia para a vítima?
# Já trabalhou com a vítima?
# O Programa deve no final emitir uma classificação sobre a participação da pesso no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser calssificada como 'Suspeita',
# entre 3 e 4 como 'Cúmplice' e 5 como 'Assassino'
# caso contrário, ele será classificado como 'Inocente'

positivos = 0

resposta = input("Telefonou para a vítima? (S ou N): ")
if resposta.upper() == 'S':
    positivos += 1

resposta = input("Esteve no local do crime? (S ou N): ")
if resposta.upper() == 'S':
    positivos += 1

resposta = input("Mora perto da vitima? (S ou N): ")
if resposta.upper() == 'S':
    positivos += 1

resposta = input("Devia para a vítima? (S ou N): ")
if resposta.upper() == 'S':
    positivos += 1

resposta = input("Já trabalhou com a vítima? (S ou N): ")
if resposta.upper() == 'S':
    positivos += 1

print(f'Positivos = {positivos}')

if positivos == 5:
    print('Assassino')
elif positivos >= 3:
    print('Cúmplice')
elif positivos == 2:
    print('Suspeito')
else:
    print('Inocente')

