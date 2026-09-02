# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h , mostre uma mensagem dizendo que ele foi multado. A multa vai custar 7,00 por cada km acima do limite.

velocidade = int(input('Qual a sua velocidade: '))
if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 7
    print('Você foi multado no valor de {}'.format(multa))

print('Você está em uma velocidade dentro do padrão!')
