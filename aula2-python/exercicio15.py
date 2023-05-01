produtos_promocao = ['Camiseta', 'Calça', 'Tênis']
percentual_desconto = 20
preco_original = 100

for produto in produtos_promocao:
    preco_promocional = preco_original - preco_original * (percentual_desconto / 100)
    print(f'{produto} - Promoção R${preco_promocional:.2f}')
