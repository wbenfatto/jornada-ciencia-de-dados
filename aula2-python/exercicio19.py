menor_idade = 0
maior_idade = 0

for i in range(1, 8):
    ano = int(input(f'Ano de nascimento da {i}º pessoa: '))
    if (2023 - ano) < 18:
        menor_idade += 1
    else:
        maior_idade += 1


print(f'Menor de idade: {menor_idade}')
print(f'Maior de idade: {maior_idade}')