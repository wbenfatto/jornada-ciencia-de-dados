import os
# limpar tela do terminal
os.system('cls')

def ler_dados():
    nome = input("Digite o nome: ")
    idade = int(input("Digite sua idade: "))
    print('O seu nome é {0} e asua idade é {1} anos.'.format(nome, idade))
    resposta = input('Deseja continuar? S/N ')
    if resposta.upper() == 'S':
        ler_dados() 


print("Digite seu dados")
ler_dados()
