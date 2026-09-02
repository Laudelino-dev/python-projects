#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
n = randint(0,5) #aqui o computador está escolhendo um numero entre 0 e 5
advinhar = int(input('Qual o valor você acha que eu escolhi?(entre 0 e 5): ')) #Aqui o jogador vai tentar advinhar o numero que a maquina selecionou
if advinhar == n:
    print('Parabens você acertou!!!')
else:
    print('A maquina venceu!!! ela escolheu o numero {} e você escolheu o numero {}'.format(n, advinhar))
