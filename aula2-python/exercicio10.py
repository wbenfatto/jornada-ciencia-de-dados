itens_pedido = {'xbacon': 15, 'refri': 8, 'batata frita': 5}

total_conta = 0

for item, valor in itens_pedido.items():
    total_conta += valor

print(f'Total a pagar: R${total_conta:.2f}')