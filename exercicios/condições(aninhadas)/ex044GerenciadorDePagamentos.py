#Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e Condição de pagamento: Á vista dinheiro/cheque:10% DE DESCONTO, Á vista no cartão:5% DE DESCONTO, em até 2x no cartão: PREÇO NORMAL, 3x ou mais no cartão: 20% DE JUROS

produto = float(input('Qual o valor do produto: '))
pagamento = input('Qual seria a forma de pagamento: DINHEIRO/CHEQUE, CARTÃO, 2x CARTÃO, 3x ou mais no CARTÃO: ').upper()
if pagamento == 'DINHEIRO' or pagamento == 'CHEQUE':
    desconto = produto * 0.10
    valor = produto - desconto
    print(f'O valor do seu produto vai ficar por R$:{valor}, com 10% de desconto!')
elif pagamento == 'CARTAO' or pagamento == 'CARTÃO':
    parcelas = input('Deseja parcelar ou sera a vista: ').upper()
    if parcelas == 'A VISTA' or parcelas == 'VISTA':
        desconto = produto * 0.05
        valor = produto - desconto
        print(f'O valor do seu produto vai ficar por R$:{valor}, com 5% de desconto!')
    elif parcelas == 'PARCELAR':
        qParcelas = int(input('Deseja parcelar em quantas vezes: '))
        if qParcelas < 1:
            print('Não é aceitavel essa forma de pagamento')
        elif qParcelas == 1:
            print('Essa forma de pagamento não é aceitavel, seria da mesma forma que pagar a vista no cartão!')
        elif qParcelas == 2:
            print(f'O valor do seu produto não vai sofrer alterações e continuara no valor de R$:{produto}')
        elif qParcelas >=3:
            juros = produto * 0.20
            valor = produto + juros
            print(f'O valor do seu produto vai ficar por R$:{valor}, com o acrescimo de 20% de juros')
    else:
        print('Não é possivel essa forma no cartão!')
else:
    print('Não foi possivel identificar esse tipo de pagamento!')
