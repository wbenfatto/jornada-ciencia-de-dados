# Faça um programa para a leitura de duas notas parciais de um aluno
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem 'Aprovado', se a média alcançada for maior ou igual a 7;
# A mensagem 'Reprovado', se a média for menor que 7;
# A mensagem 'Aprovado com Louvor', se a média for igual a 10;

nota1 = float(input('Digite a primeira nota:' ))
nota2 = float(input('Digite a segunda nota:' ))

media = (nota1 + nota2) / 2

print(f'A média desse aluno é {media}')

if media == 10:
    print("Aprovado com Louvor")
elif media >= 7:
    print('Aprovado')
else:
    print('Reprovado')


