#Crie um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra 'a', Em que posição ela aparece a primeira vez, em qual posiçao ela aparece na ultima vez

frase = str(input('Digite uma frase qualquer : ')).strip().upper()
print('Existem essa quantidades de letra a em sua frase : {}'.format(frase.count('A')))
print('A primeira letra a que aparece no caracter : {}'.format(frase.find('A')))
print('A ultima letra a aparece no caracter : {}'.format(frase.rfind('A')))
