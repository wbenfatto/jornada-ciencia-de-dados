"""
 Uma loja de roupas está fazendo uma promoção onde oferece 
 descontos de 10%  para compras acima de R$ 200,00. 
 Escreva um programa em Python que receba o valor total 
 da compra e calcule o valor final com desconto, se houver.

"""

valor_compra = float(input('Digite o valor da compra: '))

if valor_compra > 200:
    valor_compra -= valor_compra * 0.1

print(f'Valor total da compra: {valor_compra:.2f}')
