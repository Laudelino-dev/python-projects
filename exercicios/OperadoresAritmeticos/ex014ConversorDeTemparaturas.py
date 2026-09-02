# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celcius = float(input(' Digite a temperatura em Graus celcius : '))
F = (celcius * 1.8) + 32

print('{}° celcius equivalem a {}° graus farenheit'.format(celcius, F))

farenheit = float(input('Digite a temperatura em graus farenheit : '))
C = (farenheit - 32) * 5 / 9 

print('{}° graus farenheit equivalem a {}° graus celcius'.format(farenheit, C))
