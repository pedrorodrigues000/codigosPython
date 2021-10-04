""" 
for in em pyhton
Iterando strings com for
Função range(start=0, stop, step=1) 
"""
texto = 'python'
nova_string = ''

for letra in texto:
    print(letra)

print()

for numero in range (3):
    print(numero)

print()

for a in range(1, 10, 2):
    print(a)

print()

for letra in texto:
    if letra == 'p':
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)