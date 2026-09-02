# Desenvolva um programa que leia o comprimento de três retas e diga ao usuario se elas podem ou não formar um triângulo. 
l1 = float(input('Digite o tamanho do primeiro segmento de reta: '))
l2 = float(input('Digite o tamanho do segundo segmento de reta: '))
l3 = float(input('Digite o tamanho do terceiro segmento de reta: '))
if l3 < (l2 + l1) and l2 < (l3 + l1) and  l2 < (l2 + l3):
    print('os segmentos de reta formam um triangulo!!')
else:
    print('Não formam o triangulo!!')
