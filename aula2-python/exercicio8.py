# Verificar se o produto tem desconto e qual é o valor final
# produto maior igual a 100 reais tem 10%
# produto maior igual a 50 reais tem 5%

valor = float(input('Valor do produto: '))

if valor >= 100:
    valor -= valor * 0.1
elif valor >= 50:
    valor -= valor * 0.05

print(f'Valor final = {valor}')