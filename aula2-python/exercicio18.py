media = 0
soma_idades = 0
nome_mais_velho = ''
idade_mulher = 0
mais_velho = 0
counter = 0

for p in range(1, 5):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').upper()
    if sexo == 'M':
        if idade > mais_velho:
            mais_velho = idade
            nome_mais_velho = nome
    elif sexo == 'F':
        if idade < 20:
            idade_mulher += 1
    
    soma_idades += idade
    counter += 1


print(f'A média das idades é {soma_idades / counter}')
print(f'O homem mais velho é {nome_mais_velho}')
print(f'{idade_mulher} mulheres tem menos de 20 anos')