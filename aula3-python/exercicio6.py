"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um
programa que leia  um conjunto indeterminado de temperaturas em Kelvin,
e informe ao final a menor e a maior temperaturas informadas,
bem como a média das temperaturas.Para parar ele deverá informar uma temperatura negativa
"""

temperaturas = []
temperatura = 0

while temperatura >= 0:
    temperatura = float(input('Digite a temperatura em Kelvin: '))
    if temperatura >= 0:
        temperaturas.append(temperatura)

print(f'A menor temperatura é {min(temperaturas)} K')
print(f'A maior temperatura é {max(temperaturas)} K')
print(f'A temperatura média é {sum(temperaturas) / len(temperaturas)} K')