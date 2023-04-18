import os
# limpar tela do terminal
os.system('cls')

produto = input('Nome do produto: ')
valor = float(input('Valor do Produto: '))
parcela = int(input('Número de parcelas: '))

print('O {0}, custa {1:.2f} e o número de parcelas é {2}'.format(produto, valor, parcela))

parcelas = valor / parcela
print('O valor da parcela é {0:.2f}'.format(parcelas))