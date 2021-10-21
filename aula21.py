'''
Listas em Python
append,  insert, pop, del, clear, extend, +
min, max
range

'''

l2 = [4, 5, 6]

print(l2)

l2.insert(0, 3)  # insere na lista um novo indice em qualquer posição 
print(l2)

l2.pop(3)  # Deleta um indice
print(l2)

l2.append(7)  # insere na lista um novo indice ao final
print(l2)

del(l2[3])  # deleta um indice
print(l2)

print(max(l2))  #valor máximo da lista
print(min(l2))  #valor mínimo
print('------------------------')
l1 = [1,2,3,4,5,6,7,8,9]

soma = 0
for valor in l1:
    soma += valor

print(soma)
print('------------------------')

l3 = ['String', True, 10, -20.3]

for elemento in l3:
    print(f'O elemento {elemento} é do tipo {type(elemento)}')

print('------------------------')

secreto = 'funk'
digitado = []
chance = 3
while True:

    if chance <= 0:
        print('GAME OVER !')
        break

    letra = input('Digite uma letra: ')
    print()
        
    if len(letra) > 1 or letra == '':
        print('\n Você digitou nenhuma ou mais de uma letra, tente novamente 1 \n')
        continue

    digitado.append(letra)
    
    if letra in secreto:
        print(f'A letra {letra} existe na palavra \n')
    else:
        print(f'A letra não existe na palavra')
        digitado.pop()

    secreto_temporario = ''
    for letra_sereta in secreto:
        if letra_sereta in digitado:
            secreto_temporario += letra_sereta
        else:
            secreto_temporario += '_'
            print()
    
    if secreto_temporario == secreto:
        print('PARABÉNS VOCÊ DESCOBRIU A PALAVRA\n')
        print(f'palavra secreta era {secreto}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}\n')
    
    if letra not in secreto:
        chance -= 1
    if letra in secreto:
        print(f'Você acertou te resta apenas {chance} chances \n')
    elif letra not in secreto:
        print(f'Você errou restam apenas {chance} chances')

    print(secreto_temporario)
