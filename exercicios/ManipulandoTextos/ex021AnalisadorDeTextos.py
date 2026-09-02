#Crie um programa que leia um nome completo de uma pessoa e mostre na tela : o nome com todas as letras maisculas , o nome com todas as letras minusculas, quantas letras ao todo(sem considerar espaços), quantas letras tem o primeiro nome

nome = str(input('Qual seu nome completo : '))
print('Seu nome completo em letras maisculas fica : {}'.format(nome.upper()))
print('Seu nome completo em letras minusculas fica : {}'.format(nome.lower()))
print('Somente seu nome contem essa quantidade de caracteres : {}'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e contém essa quantidade de letras : {}'.format(nome.split() [0], len(nome.split()[0])))
