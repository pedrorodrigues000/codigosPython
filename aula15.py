'''
Faça um programa que ao digitar um número inteiro ele informe se é par ou ímpar. Caso o numero inserido 
não for inteiro, informar.
'''
numero = input('Digite um número inteiro: ')


if numero.isdigit():
    pass
    
    numero = int(numero)

    if numero % 2 == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} é ímpar')

else:
    print('Isso não é um número')

'''
Faça um programa que peça o horário, e baseando-se na hora descrita informe a saudação apropriada
ex: 0 - 11 horas = Bom dia; 12 - 17 = Boa tarde; 18 - 23 = Boa noite
'''

horas = input('Digite o horário entre 0 e 23: ')

if horas.isdigit():
    pass

    horas = int(horas)

    if horas < 0 or horas > 23:
        print("Digite um horário entre 0 e 23")
    else:
        if horas <= 11:
            print('Bom Dia !!')
        elif horas <= 17:
            print('Boa Tarde !!')
        else:
            print('Boa Noite !!')
else:
    print('O dado inserido não corresponde um horário')




'''
Faça um programa que leia o nome e diga: se o nome tem até 4 letrar (O nome é pequeno)
se tem de 5 a 6 letras (o nome é normal)
acima de 6 (seu nome é grande)
'''
nome = input('Digite seu nome: ')
qtd = len(nome)

if qtd > 0 and qtd <=4:
    print('Seu nome é pequeno')
elif qtd > 4 and qtd <=6:
    print('Seu nome é normal')
else:
    print('Seu nome é grande')
