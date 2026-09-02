# Desafio 7 
# Desenvolva um programa que leia duas notas de um aluno e calcule a sua media

n1 = float(input('Qual a sua primeira nota : '))
n2 = float(input('Qual a sua segunda nota : '))
media = (n1+n2)/2
print('As repectivas notas do aluno foi {:.2f} e {:.2f}, e sua media foi de {:.2f}.'.format(n1, n2, media))
