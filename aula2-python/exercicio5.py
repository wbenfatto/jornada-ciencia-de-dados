# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#               Até 5kg         Acima de 5kg
# Morango       R$ 2,50/kg      R$2,20/kg
# Maçã          R$ 1,80/kg      R$1,50/kg

# Se o cliente comprar mais de 8kg em frutas ou o valor total da compra 
# ultrapassar R$25,00 receberá um desconto de 10% sobre o total
# Escreva um algoritmo para ler a quantidade (em kg) de morangos e a
# quantidade (em kg) de maçãs adquiridas e escreva o valor a ser pago pelo cliente.

morango = float(input('Kg de morangos: '))
maca = float(input('Kg de maçã: '))

valor = 0

if morango <= 5:
    valor = morango * 2.5
else:
    valor = morango * 2.2

if maca <= 5:
    valor = maca * 2.5
else:
    valor = maca * 2.2


if (morango + maca) > 8 or valor > 25:
    valor -= (valor * 0.1)

print(f'Quantidade de morangos: {morango}kg, com valor total de R${morango}')
print(f'Quantidade de maçãs: {maca}kg, com valor total de R${maca}')
print(f'Valor total: R${valor:.2f}')