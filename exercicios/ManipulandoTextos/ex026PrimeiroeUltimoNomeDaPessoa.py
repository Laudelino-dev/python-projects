#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguinda o primeiro e o ultimo nome separadamente

nome = str(input('Digite seu nome completo : ')).strip().split()
print('Primeiro nome : {}'.format(nome [0]))
print('Ultimo nome : {}'.format(nome [-1]))
