#Retornar a tabuada de um número inteiro, parar com um número negativo

while True:
    n = int(input('Qual tabuada você quer? '))
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n} x {i} = {i * n}')