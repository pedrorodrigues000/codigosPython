'''
Formatação de string (introdução)

'''
nome = 'Pedro'
idade = 20
peso = 109 
altura = 1.80
imc= peso / altura**2
ano = 2021
nascimento = ano - idade

print(f'O Sr {nome} nascido no ano de {nascimento} , com idade atual de {idade}, possui imc de {imc:.2f}')
