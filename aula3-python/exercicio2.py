# Solicitar que a pessoa digite o sexo, se for diferente de M ou F,
# solicitar que digite novamente.

sexo = input('Digite o sexo (M/F): ').upper().strip()[0]

while sexo not in "MF":
    sexo = input('O valor de sexo deve ser F ou M: ').upper().strip()[0]

print(f'O valor do sexo selecionado foi {sexo}')