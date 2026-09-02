# Desafio08
# Faça um programa que leia um valor em metros e converta ele em centimetros e milimetros.

n = float(input('Digite sua distância em metros : '))
dc = n * 10
c = n * 100
m = n * 1000

dam = n / 10
hm = n / 100
km = n / 1000

print('Seu valor em metros é {},\n ele em centrimetos fica {}\n e em milimetros fica {}.'.format(n, c, m))
print('Seu valor em decimentros fica {}'.format(dc))
print('Seu valor em decâmetro é {} \nSeu valor em hectômetro é {}\n Seu valor em Kilômetro é {}'.format(dam, hm, km))
