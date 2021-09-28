'''
Quantidade de caractres

'''
usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)


if qtd_caracteres == 6:
    print('O usuario está correto')
else:
    print(f'Usuario possui somente {qtd_caracteres} letras')


