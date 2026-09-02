#Desenvolva uma logica que leia o peso e altura de uma pessoa,calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#Abaixo de 18.5:ABAIXO DO PESO, entre 18.5 e 25:PESO IDEAL, 25 até 30:SOBREPESO, 30 até 40: OBESIDADE, acima de 40: OBESIDADE MORBIDA

peso = float(input('Informe o seu peso: '))
altura = float(input('informe sua altura: '))
imc = peso / (altura**2)
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc >= 18.5 and imc <= 25:
    print('Você está no peso ideal!')
elif imc >25 and imc <= 30:
    print('Você está em sobrepeso!')
elif imc >30 and imc <=40:
    print('Você está com obesidade!')
else:
    print('Você está com obesidade morbida!')
