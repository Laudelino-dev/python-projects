# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice
aluno1 = input('Primeiro aluno : ')
aluno2 = input('Segundo aluno : ')
aluno3 = input('Terceiro aluno : ')
aluno4 = input('Quarto aluno : ')
escolha = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(escolha)
print('O aluno escolhido foi {} '.format(escolhido))
