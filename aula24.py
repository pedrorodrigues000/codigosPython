'''
Operador ternário
'''

login_bd = 'Pedro'
senha_bd = 1234

login = input('Login: ')
senha = input('Senha: ')

if not senha.isnumeric():
    print('Digite apenas numeros')
else:
    message = 'Usuário logado' if login == login_bd and senha == senha_bd else 'Senha ou usuário incorretos !'

  

