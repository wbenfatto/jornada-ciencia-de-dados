"""
Uma loja precisa calcular o valor final de uma compra, 
considerando que há um desconto de 10% para compras acima de R$ 100,00 
e um acréscimo de 5% para compras parceladas em 3 vezes. 
Escreva um programa em Python que receba o valor total da compra 
e a forma de pagamento (à vista ou parcelado em 3 vezes) 
e calcule o valor final com os devidos descontos ou acréscimos.

"""

valor_total = float(input('Qual o valor total da compra? '))
forma_pagamento = input('Qual a forma de pagamento? v = à vista, p = à prazo: ')

if valor_total > 100:
    valor_total -= valor_total * 0.1
    print(f'10% de desconto aplicado.')

if forma_pagamento.lower() == 'p':
    parcelas = int(input('Será parcelado em quantas vezes? '))
    if parcelas == 3:
        valor_total += valor_total * 0.05
        print(f'5% de acréscimo aplicado.')


print(f'Valor a pagar: {valor_total:.2f}')
