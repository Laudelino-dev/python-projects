#Escreva um programa que leia dois numeros inteiros e compares-os, mostrando na tela uma mensagem: o Primeiro valor é maior, o segundo valor e maior , não existe valor maior, os dois são iguais
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
if num1 > num2:
    print('O primeiro valor é maior!')
elif num2 > num1:
    print('O Segundo valor é o maior!')
else:
    print('Os dois são iguais!')
