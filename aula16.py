'''
formatando valores com modificadores

:s (string)
:d (inteiros)
:f (float)
:.(numero) f - selecionar quantidade de casas decimais
:(caractere) (> ou < ou ^) (quantidade) (tipo - s, d ou f)

< - esquerda
> - direita
^ - centro

'''
num1 = 10
num2 = 3
num3 = 20
num4 = 3
divisao1 = num1 / num2 
divisao2 = num3 / num4

print('{:.2f}'.format(divisao1))

print(f'{divisao2:.2f}')
print()

a = 1
print(f'{a:0>10}')

b = 1500
print(f'{b:0>10}')
print()

nome = 'Pedro'
print(f'{nome:#>7}')
