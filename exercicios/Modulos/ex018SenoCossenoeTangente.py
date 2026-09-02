# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seu seno,cosseno e tangente desse angulo.

#Para calculo de angulo na biblioteca Math o seno, cosseno e tangente são em radianos, como utilizamos angulos devemos  utilizar a função RADIANS para realizar esse calculo de angulo, como fizemos da forma abaixo.

from math import cos, sin, tan, radians
angulo = float(input('Informe o ângulo : '))
cos =  cos(radians(angulo))
sen = sin(radians(angulo))
tan = tan(radians(angulo))
print('Cosseno do angulo é {:.2f}'.format(cos))
print('Seno do angulo é {:.2f}'.format(sen))
print('Tangente do angulo é {:.2f}'.format(tan))
