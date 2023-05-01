transacoes = [100, -50, 300, -200, 50]

saldo = 0

for transacao in transacoes:
    saldo += transacao

print('O saldo da conta é de R${}'.format(saldo))