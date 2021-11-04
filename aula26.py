'''
Funções - def 
'''

def funcao (msg='PLANETA'):
    msg = msg.replace('A', '4')
    msg = msg.replace('E', '3')

    print(msg)

funcao()
print()

def outro_valor (var):
    return var

variavel = outro_valor('Feito com return')

if outro_valor:
    print(variavel)
else:
    print('ADEUS')

print()

def conta (n1,n2):
    if n1 == 0 and n2 == 0:
        return
    return n1 * n2

multi = conta(50, 2)
if multi:
    print(multi)
else:
    print('***')

print()

def A(var):
    print(var)

def retorna():
    return A

var = retorna()
var = ('XXXX')
print(var)

print()

def args(*args, **kwargs):
    print(args)

    idade = kwargs ['idade']
    print(idade)

list1 = [1,2,3,4,5,6]
list2 = [6,5,4,3,2,1]
args(*list1, *list2, nome='Pedro', sobrenome='Henrique', idade=20)
