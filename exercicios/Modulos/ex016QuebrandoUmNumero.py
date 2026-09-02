# Crie um programa que leia um numero Real qualquer e mostre na  tela a sua porção inteira.

# Ex: Digite um número 6.127 tem a parte inteira 6.

from math import trunc
num = float(input('Digite um número real : '))
print('O numero real que você informou é {}, e sua parte inteira é {}'.format(num, trunc(num)))
