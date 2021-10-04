frase = 'python é uma ótima linguagem'
tamanho = len(frase)
contador = 0
nova = ''
digito = input('Digite a letra que deseja ser maiúscula: ')


while contador < tamanho:
    letra = frase[contador]
    if letra == digito:
        nova += digito.upper()
    else:
        nova += letra
    contador += 1

print(nova)
    
