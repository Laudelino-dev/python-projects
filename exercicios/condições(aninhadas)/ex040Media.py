#Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com a média atingida: media abaixo de 5.0:REPROVADO, média entre 5.0 e 6.9:RECUPERAÇÂO, Média 7.0 ou superior: APROVADO

nota1 = float(input('Qual a sua primeira nota: '))
nota2 = float(input('Qual a sua segunda nota: '))
media = (nota1 + nota2) /2
if media < 5:
    print('REPROVADO')
elif media >= 5 and media <6.9:
    print('Recuperação')
elif media > 7:
    print('APROVADO')
