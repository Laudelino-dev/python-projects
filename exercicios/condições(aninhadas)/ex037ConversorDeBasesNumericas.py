#Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual será a base da conversão: 1 para binário, 2 para octal 3 para hexadecimal

num = int(input('Digite o valor: '))
conversão = int(input('Qual será sua base para conversão: 1 PARA BÍNARIO, 2 PARA OCTAL, 3 PARA HEXADECIMAL: '))
if conversão == 1:
    binario = bin(num)
    print(f'Aqui é seu numero escrito em forma binaria: {binario[2:]}')
elif conversão == 2:
    octal = oct(num)
    print(f'Aqui é seu numero escrito em forma octal: {octal[2:]}')
elif conversão == 3:
    hexadecimal = hex(num)
    print(f'Aqui é seu numero escrito em forma Hexadecimal: {hexadecimal[2:]}')
else:
    print('Não possuimos essa forma de conversão')
