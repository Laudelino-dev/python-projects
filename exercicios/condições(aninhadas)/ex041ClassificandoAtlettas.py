#A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: Até 9 anos:MIRIM, Até 14 anos:INFATIL, Até 19 anos:JUNIOR, Até 20 anos: SÊNIOR, Acima: MASTER.

from datetime import date
anoDeNascimento = int(input('Informe seu ano de nascimento: '))
anoAtual = date.today().year
categoria = anoAtual - anoDeNascimento
if categoria <= 9:
    print('Você faz parte da categoria MIRIM!')
elif categoria > 9 and categoria <= 14:
    print('Você faz parte da categoria INFANTIL')
elif categoria > 14 and categoria <= 19:
    print('VOcê faz parte da categoria JUNIOR')
elif categoria == 20  :
    print('Você faz parte da categoria SÊNIOR')
else :
    print('Você faz parte da categoria MASTER')
