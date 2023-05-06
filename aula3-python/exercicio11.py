# Cadastrar o nome e a idade de pacientes
# se tiver mais de 60 anos, enviar um alerta
# perguntar se quer continuar cadastrando

while True:
    nome = input('Digite o nome do paciente: ')
    idade = int(input('Digite a idade do paciente: '))

    print(f'Paciente {nome} tem {idade}')
    if(idade > 60):
        print('Atenção: Paciente com mais de 60 anos.')

    parar = input('Deseja parar? (S/N) ').upper()
    if parar == 'S':
        break