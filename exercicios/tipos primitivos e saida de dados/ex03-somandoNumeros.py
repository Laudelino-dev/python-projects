#desafio 3

n1=int(input('Digite o primeiro numero: '))
n2=int(input('Digitie o segundo numero: '))
s=n1+n2
print('A soma dos 2 numeros informados resulta em:',s)

#Outra forma de sintaxe de print

print('A soma dos 2 numeros informados resulta em: {}'.format(s))

# desafio extra

print('A soma entre',n1, 'e', n2,'resulta em:',s)

#Com a nova sintaxe

print('A soma entre {} e {} resulta em {}'.format(n1, n2, s))
