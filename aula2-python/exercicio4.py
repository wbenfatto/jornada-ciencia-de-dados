# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool: até 20 litros, desconto de 3% por litro acima de 20 litros, desconto de 5% por litro
# Gasolina: até 20 litros, desconto de 4% por litro acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos
# O tipo de combustível (A = Alcool, G = Gasolina)
# Calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço por litro
# da gasolina é de R$ 2,50 e o preço do litro do alcool é R$1,90

litros = float(input('Digite quantos litros você quer abastecer: '))
combustivel = input('Digite A para alcool ou G para gasolina: ').upper()
preco = 0

if combustivel == 'A':
    preco = litros * 1.9
    if litros <= 20:
        preco -= (1.9 * litros) * (3 / 100)
    else:
        preco -= (1.9 * litros) * (5 / 100)
elif combustivel == 'G':
    preco = litros * 2.5
    if litros <= 20:
        preco -= (2.5 * litros) * (4 / 100)
    else:
        preco -= (2.5 * litros) * (6 / 100)

print(f'O preço que você vai pagar é de R${preco:.2f}')