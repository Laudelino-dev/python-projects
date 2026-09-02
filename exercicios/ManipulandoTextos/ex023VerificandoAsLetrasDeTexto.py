#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'

cidade = str(input('Qual o nome da sua cidade : ')).strip().split()
print('Sua cidade começa com santo : {}'.format( 'SANTO' in cidade[0].upper()))
