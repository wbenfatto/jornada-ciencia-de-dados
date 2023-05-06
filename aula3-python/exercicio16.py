""""
Crie um programa que verifica se uma pessoa pode se aposentar.
Para se aposentar, é preciso ter mais de 60 anos 
ou ter mais de 30 anos de contribuição ao INSS.
"""

idade = int('Qual a sua idade? ')
contribuicao = int('Quantos anos de contribuição ao INSS? ')

if idade > 60 or contribuicao > 30:
    print('Pode se aposentar')
else:
    print('Não pode se aposentar')
