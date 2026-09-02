print('-' * 36)
print(' Bem vindo ao verificador de senha!')
print('-' * 36)
print('''A senha deve conter algumas Requerimentos essenciais para ser aceita:
         Deve conter no minimo 8 caracteres
         Deve conter no minimo 1 letra Maiscúla
         Deve conter no minimo 1 letra Minuscula
         Deve conter no minimo 1 Caracter especial.''')

senha = input('Digite uma senha: ').strip() # Solicitando a senha para o usuario.

maisculo = senha != senha.lower() # Verificando se possui letra maiscúla na senha.
minusculo = senha != senha.upper() # Verificando se possui letra minúscula na senha.
caracter = len(senha) >= 8 # Verificando se possui no minimo 8 caracteres na senha.
número = '0' in senha or '1' in senha or '2' in senha or '3' in senha or '4' in senha or '5' in senha or '6' in senha or '7' in senha or '8' in senha or '9' in senha
cEspecial = '!' in senha or '@' in senha or '#' in senha or '%' in senha or '&' in senha or '*' in senha

if maisculo and minusculo and caracter and número and cEspecial:
    print('Sua senha foi validada! é uma senha segura!')
else:
    print('Sua senha não atende os Requerimentos minimos! Tente novamente')
    if not maisculo:
        print('Sua senha precisa ter no minimo 1 caracter maiscúlo.')
    if not minusculo:
        print('Sua senha precisa ter no minimo 1 caracter minúsculo.')
    if not caracter:
        print('Sua senha precisa ter no minimo 8 caracteres.')
    if not número:
        print('Sua senha precisa ter no minimo 1 número.')
    if not cEspecial:
        print('Sua senha precisa ter no minimo 1 caracter especial.')
