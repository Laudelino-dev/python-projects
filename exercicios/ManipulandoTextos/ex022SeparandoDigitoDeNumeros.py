# Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados. EX: Digite um numero : 1832,  Unidade:2 , dezena:3 , centena:8, milhar:1

numero = int(input('Digite um numero qualquer entre 0 e 9999 : '))
u = numero // 1 % 10
c = numero // 10 % 10
d = numero // 100 % 10
m = numero // 1000 % 10
print('Unidade : {}'.format(u))
print('centena : {}'.format(c))
print('dezena : {}'.format(d))
print('milhar : {}'.format(m))
