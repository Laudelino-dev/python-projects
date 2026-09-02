# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.

from math import sqrt
co = float(input('Informe qual o comprimento do cateto oposto : '))
ca = float(input('Informe qual o comprimento do cateto adjacente : '))
h = sqrt(co**2 + ca**2)
print('Os angulos informados são {} e {}, e sua hipotenusa é {:.2f}'.format(co, ca, h))
