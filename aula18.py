'''
While em python
utilizando para realizar ações enquanto um condição for verdadeira
'''
x = 0 

while x < 5:
    y = 0
    while y < 3:
        print (f'({x}, {y})')
        y+=1
    x+=1
    
print('Contagem finalizada !')
 
while True :
    print()
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')
    sair = input('Deseja sair ? [s] ou [n]')

    if not num1.isnumeric() or not num2.isnumeric():
        print()
        print('Você precisa digitar um número ')
        
    if sair == 's':
        print('Até logo')
        break

    num1 = int(num1)
    num2 = int(num2)

    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '/':
        print(num1 / num2)
    elif operador == '*':
        print(num1 * num2)
    else:
        print('Operador inválido')
