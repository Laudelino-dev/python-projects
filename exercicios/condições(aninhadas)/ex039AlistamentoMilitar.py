#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: Se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar, se já passou do tempo do alistamento. O programa também deve mostrar o tempo que falta ou passou do prazo.

from datetime import date 
anoDeNascimento = int(input('informe o seu ano de nascimento: ')) # pedindo ao usuario para informar seu ano de nascimento 
anoAtual = date.today().year #importando o ano atual configurado na maquina 
alistamento =  anoAtual - anoDeNascimento #subtraindo o ano atual do ano de nascimento 
if alistamento < 18 : #aqui definindo que se o usuario tiver menos de 18 anos ele não podera se alistar no exercito ainda
    tempo = (18 - alistamento) * 12
    print('Você ainda não possui a idade suficiente para se alistar!')
    print(f'Ainda faltam {tempo} meses para você se alistar!')
elif alistamento == 18 : #aqui definindo que se o usuario tiver a idade de 18 anos ele está no periodo de se alistar no exercito 
    print('Você está na fase de alistamento militar!')
else: # aqui defininto que de ele estiver mais de 18 anos ele ja passou do periodo de se alistar 
    tempo = (alistamento - 18)
    resultado = tempo * 12 
    print('Você já passou da idade de se alistar!')
    print(f'Você passou do prazo num periodo de {resultado} meses!')
