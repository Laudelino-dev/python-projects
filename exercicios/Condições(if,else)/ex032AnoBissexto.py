# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
ano = int(input('Qual o ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0 :
    ano = date.today().year # pegar o ano atual da maquina
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano de {ano} é bissexto')
else:
    print(f'o ano de {ano} não é bissexto')

