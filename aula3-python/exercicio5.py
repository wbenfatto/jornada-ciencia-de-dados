# Simular um caixa eletronico
# Qual valor será sacado
# Informar quantas células de cada valor será entregue
# Possui cédulas de 50, 20, 10, 1

saque = int(input('Valor a ser sacado: '))
notas = [50, 20, 10, 1]
cedulas = []

while saque > 0:
    for val in notas:
        cedulas.append(saque // val)
        saque = saque % val

counter = 0

for item in cedulas:
    if item > 0:
        print(f'{item} cédulas de R$ {notas[counter]}')
    counter += 1
    

