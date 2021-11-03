def saudacao (s1='Olá', n1='Senhor'):
    print(s1, n1)

saudacao()

print()

def numeros (n1,n2,n3):
    return n1 + n2 + n3

num = numeros(1,1,1)
print(f'{num}\n')

def valor(n1,n2):
    if n2 >=0 and n2 <=100:
        return (n2 / 100) * 100 + n1 
        
    else:
        print('Valor inserido inválido')

valor_final = valor(10,100)
print(f'{valor_final}% \n')

def fizz_buzz(v1):
    if v1 % 2 == 0:
        return 'Fizz'
    elif v1 % 3 == 0 and v1 % 5 == 0:
       return 'FizzBuzz'
    elif v1 % 5 == 0:
        return 'Buzz'
    else:
        return v1

div = fizz_buzz(9)
print(div)
