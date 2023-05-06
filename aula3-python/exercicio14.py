"""
Crie um programa que pergunte ao usuário se ele é estudante 
e se tem menos de 18 anos. Se o usuário for estudante e tiver menos de 18 anos, 
imprima "Você tem direito à meia-entrada", caso contrário, 
imprima "Você não tem direito à meia-entrada".
"""

estudante = input('É estudante? (s/n): ').lower()
idade = int(input('Qual a idade: '))

if(estudante == 's' and idade < 18):
    print("Você tem direito à meia-entrada")
else:
    print("Você não tem direito à meia-entrada")

