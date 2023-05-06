#Faça um programa que simule uma corrida entre dois carros. 
#O programa deve solicitar ao usuário a velocidade dos carros 
#e a distância da pista. O laço deve continuar até que 
#um dos carros chegue ao final da pista. Ao finalizar a corrida, o programa deve exibir o vencedor.

distancia = float(input('Quantos km tem a pista? '))
velocidade_carro_1 = float(input('Qual a velocidade do 1º carro: '))
velocidade_carro_2 = float(input('Qual a velocidade do 2º carro: '))

posicao_carro_1 = 0
posicao_carro_2 = 0

while posicao_carro_1 < distancia and posicao_carro_2 < distancia:
    posicao_carro_1 += velocidade_carro_1
    posicao_carro_2 += velocidade_carro_2

if posicao_carro_1 > posicao_carro_2:
    print('Carro 1 Venceu')
elif posicao_carro_2 > posicao_carro_1:
    print('Carro 2 venceu')
else:
    print('Empate')

