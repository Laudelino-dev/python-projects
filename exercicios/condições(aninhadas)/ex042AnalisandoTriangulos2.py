#Reforça o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será formado: Equilatero:TODOS OS LADOS IGUAIS, isóceles:DOIS LADOS IGUAIS, Escaleno:TODOS OS LADOS DIFERENTES.

lado1 = float(input('Informe o tamanho do segmento de reta: '))
lado2 = float(input('Informe o tamanho do segundo segmento de reta: '))
lado3 = float(input('Informe o tamanho do terceiro segmento de reta: '))
if lado1 < (lado2 + lado3) and lado2 < (lado1 + lado3) and lado3 < (lado1 + lado2):
    print('Os lados formam um triangulo')
    if lado1 == lado2 and lado1==lado3:
        print('Eles formam um triangulo EQUILATERO')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Eles formam um triangulo ISÓCELES')
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print('Eles formam um triangulo ESCALENO')
else:
    print('Eles não forman um triangulo!')
