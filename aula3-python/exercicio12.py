# salao de beleza, pedir o nome do cliente e o serviço
# continuar perguntando até encerrar

while True:
    nome = input('Digite seu nome: ')
    servico = input('Digite o serviço que você deseja corte de cabelo ou manicure: ')

    print(f'O serviço de {servico} foi marcado para {nome}')

    continuar = input('Deseja continuar? s/n').lower()
    if continuar != 's':
        break
