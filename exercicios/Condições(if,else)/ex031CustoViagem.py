# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando 0,50 por km para viagens de até 200km e 0,45 para viagens mais longas.

km = float(input('Qual a distancia que você irá percorrer: '))
if km <= 200:
    valor = km * 0.50
    print('O valor da sua passagem é de R$:{}'.format(valor))
else:
    valor2 = km * 0.45
    print('O valor da sua passagem é de R$:{}'.format(valor2))
