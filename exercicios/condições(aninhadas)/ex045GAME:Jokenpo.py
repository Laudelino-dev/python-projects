#Crie um programa que faça o  computador jogar JOKENPO com você.
from random import choice 
jokenpo = ['PEDRA', 'PAPEL', 'TESOURA']
maquina = choice(jokenpo)

print('-'*22)
print(' Vamos jogar JOKENPO')
print('-'*22)

escolha = input('Qual você escolhe: PEDRA,PAPEL ou TESOURA: ').upper()
if escolha == 'PEDRA' and maquina == 'TESOURA':
    print(f'PARABENSS,VOCÊ GANHOU!!!, A maquina escolheu:{maquina} e você escolheu:{escolha}')
elif escolha == 'PEDRA' and maquina == 'PAPEL':
    print(f'Infelizmente você perdeu!, A maquina escolheu:{maquina} e você escolheu:{escolha}')
elif escolha == 'PEDRA' and maquina == 'PEDRA':
    print(f'Aconteceu um empate!, A maquina escolheu:{maquina} e você escolheu:{escolha}')
elif escolha == 'PAPEL' and maquina == 'TESOURA':
    print(f'Infelizmente você perdeu, A maquina escolheu:{maquina} e você escolheu:{escolha}')
elif escolha == 'PAPEL' and maquina == 'PAPEL':
    print(f'Aconteceu um empate!, A maquina escolheu:{maquina} e você escolheu:{escolha}')
elif escolha == 'PAPEL' and maquina == 'PEDRA':
    print(f'PARABENSS,VOCÊ GANHOU!!!, A maquina escolheu:{maquina} e você escolheu:{escolha}')
elif escolha == 'TESOURA' and maquina == 'TESOURA':
    print(f'Aconteceu um empate!, A maquina escolheu:{maquina} e você escolheu:{escolha}')
elif escolha == 'TESOURA' and maquina == 'PAPEL':
    print(f'PARABENSS,VOCÊ GANHOU!!!, A maquina escolheu:{maquina} e você escolheu:{escolha}')
elif escolha == 'TESOURA' and maquina == 'PEDRA':
    print(f'Infelizmente você perdeu, A maquina escolheu:{maquina} e você escolheu:{escolha}')
else:
    print(f'A opção que você escolheu é invalida!!!, você digitou: {escolha}')
