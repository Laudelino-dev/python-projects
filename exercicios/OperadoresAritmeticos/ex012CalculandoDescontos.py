# desafio 12
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

preco = int(input('Informe  o valor do produto : R$ '))
liquidacao = preco * 0.05
preco_final = preco - liquidacao

print('O valor do produto que você informou, na liquidação ele terá o preço de : {}, com um desconto de 5%.'.format(preco_final))

all= preco*5/100
pf = preco - all
print(pf)
