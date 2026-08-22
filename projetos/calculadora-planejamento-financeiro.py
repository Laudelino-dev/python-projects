print('-' * 60 )
print('  Olá, Seja bem vindo ao calculo de gasto ideal de salario')
print('-' * 60 )
print('  Existem 2 tipos de formas para se calcular os gastos de salario \n ' \
' Existe o tipo mais utilizado que seria o modo 50-30-20, onde A: \n' \
'   50% para Necessidades( Contas fixas e vitais como aluguel, luz, água, mercado, saúde e transporte.) \n' \
'   30% para Desejos( Gastos com lazer, restaurantes, passeios e compras pessoais.) \n' \
'   20% para o Futuro( Dinheiro guardado para investimentos, reservas de emergência ou quitar dívidas.) \n' \
' E também existe o modo menos "convencional" 70-20-10, onde B: \n' \
'   70% para Essencial(Contas fixas e vitais como aluguel, luz, água, mercado, saúde e transporte, etc.) \n' \
'   20% para Supérfluos( Gastos com lazer, restaurantes, passeios e compras pessoais.) \n' \
'   10% para o Investimentos (Dinheiro guardado para investimentos.)')
print('-' * 60 )

from time import sleep # Importando a função sleep para fazer o programa atrasar alguns segundos onde eu desejo.

salario = float(input('Informe seu salario atual R$:')) # Solicitando ao usuario informar o seu salario e definindo do tipo float pois é um valor real.
tipo = input('Qual a forma de calculo que você deseja: ').upper() # Pedindo para informar o tipo de calculo que o usuario iria querer das informadas acima
print('-' * 18)
print('Analisando dados')
print('-' * 18)
sleep(1) # Atrasando o programa em 1 segundo
if tipo == 'A': # Aqui se inicia o calculo sendo na opcão A
    necessidades = salario * 0.50
    desejos = salario * 0.30
    futuro = salario * 0.20
    print(f'O valor para gastos com Necessidades é de: R${necessidades} \n'
          f'O valor para gastos com Desejos é de: R${desejos} \n'
          f'O valor para gastos com o Futuro é de: R${futuro}')
elif tipo == 'B': # Aqui se inicia o calculo sendo na opcão B
    essencial = salario * 0.70
    superfluo = salario * 0.20
    investimentos = salario * 0.10
    print(f'O valor para gastos com o Essencial é de: R${essencial} \n'
          f'O valor para gastos com os Supérfluos é de: R${superfluo} \n'
          f'O valor para gastos com os Investimentos é de: R${investimentos}')
elif tipo != 'A' and tipo != 'B': # Aqui é caso o usuario não informe nenhuma das opções configuradas acima.
    print('O tipo informado não está cadastrado no nosso sistema, encerrando o programa...')
    sleep(2)
    print('-' * 18)
    print('PROGRAMA ENCERRADO!!!')
    print('-' * 18)
