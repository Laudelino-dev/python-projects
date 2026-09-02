# Desafio05
# leia um numero e mostre seu valor antecessor e sucessor

n1 = int(input(' Me informe um valor : '))
a = n1 - 1
s = n1 + 1 
print('O numero que você escolheu é {} o seu antecessor é {} e o seu sucessor é {}.'.format(n1, a, s))

# mais compacto
n = int(input('Digite um numero : '))
print('O numero escolhido foi {}, seu antecessor é {}, e seu sucessor é {}'.format(n, (n-1), (n+1)))
