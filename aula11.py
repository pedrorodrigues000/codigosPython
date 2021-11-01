'''
Operadores Lógigos

E - and
OU - or
Não - not
in e not in

'''
num1 = 1
num2 = 2
num3 = 2
num4 = 4
'''
# o and aceita somente condições verdadeiras para o valor ser TRUE
print(num1 == num2 and num2 != num1)

# o or aceita a partir de uma condição verdadeira para retornar valor true
print(num2 != num3 or num2 != num4)

if not num1 > num4:
    print('Maior q num4')
else:
    print('Menor q num4')

print()
nome = 'pedro'

if 'd'  in nome:
    print('existe a letra d no nome')
else: 
    print('não existe')
'''
print('\n')

usuario_bd = 'Pedro'
senha_db = 1234

usuario = input('Usuário: ')
senha = int(input('Senha: '))

if usuario == usuario_bd and senha == senha_db:
    print('Você está logado no sistema')
   
else :
    print('Usuário ou senha incorretos \n')
