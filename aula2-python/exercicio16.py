pacientes = [{'nome': 'Ana', 'idade': 35}, {'nome': 'João', 'idade': 42}, {
    'nome': 'Pedro', 'idade': 28}, {'nome': 'Maria', 'idade': 50}]

for paciente in pacientes:
    print('{} tem {} anos'.format(paciente['nome'], paciente['idade']))