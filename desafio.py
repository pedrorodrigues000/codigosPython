'''
Existem 5 motoboys, cada motoboy ganha uma comissão diferente por pedido coletado, e alguns motoboys possuem exclusividade com algumas lojas na qual fazem coletas.

Os motoboys não podem reclamar que ficaram sem pedidos.

Os motoboys que possuem exclusividade com as lojas, possuem prioridade.

Os motoboys podem ter exclusividade com as lojas, mas as lojas não possuem exclusividade com os motoboys.

Hoje existem 10 pedidos para serem retirados em 3 lojas.

Quando eu executar o script passando apenas o motoboy ou não passando nenhum motoboy, preciso ver:
Quem é o motoboy e quantos pedidos terá?
De qual loja é?
Quanto vai ganhar?

Dados do teste

Motoboys
Moto 1 - cobra R$2 reais por entrega e atende todas as lojas
Moto 2 - cobra R$2 reais por entrega e atende todas as lojas
Moto 3 - cobra R$2 reais por entrega e atende todas as lojas
Moto 4 - cobra R$2 reais por entrega e atende apenas a loja 1
Moto 5 - cobra R$3 reais por entrega e atende todas as lojas

Lojas
m1,m2,m4 -Loja 1 - 3 pedidos (PEDIDO 1 R$50, PEDIDO 2 R$50, PEDIDO 3 R$50) e paga 5% do valor pedido por entrega fora o valor fixo. 
m1,m2,m3,m5 -Loja 2 - 4 pedidos (PEDIDO 1 R$50, PEDIDO 2 R$50, PEDIDO 3 R$50, PEDIDO 4 R$50) e paga 5% do valor pedido por entrega fora o valor fixo.
m3,m5Loja 3 - 3 pedidos (PEDIDO 1 R$50, PEDIDO 2 R$50, PEDIDO 3 R$100) e paga 15% do valor pedido por entrega fora o valor fixo.

O Moto 1 atende todas as lojas
O Moto 2 atende todas as lojas
O Moto 3 atende todas as lojas
O Moto 4 atende apenas a loja 1
O Moto 5 atende todas as lojas
'''
""" l1 = m1, m2, m4
l2 = m1, m2, m3, m5
l3 = m3, m5 """

l1 = 'Loja 1'
l2 = 'Loja 2'
l3 = 'Loja 3'

preco_m1 = (350 * 0.05) + 350 + 2
preco_m2 = (350 * 0.05) + 350 + 2
preco_m3 = 400 * 0.2 + 2
preco_m4 = 150 * 0.05 + 2
preco_m5 = 400 + 0.2 + 3

pedido_m1 = f'2 pedidos \n valor ganho: R${preco_m1} \n entregue nas lojas: {l1} e {l2}'
pedido_m2 = f'2 pedidos \n valor ganho: R${preco_m2} \n entregue nas lojas: {l1} e {l2}'
pedido_m3 = f'2 pedidos \n valor ganho: R${preco_m3} \n entregue nas lojas: {l2} e {l3}'
pedido_m4 = f'1 pedidos \n valor ganho: R${preco_m4} \n entregue nas lojas: {l1}'
pedido_m5 = f'2 pedidos \n valor ganho: R${preco_m5} \n entregue nas lojas: {l2} e {l3}'

dados1 = f'O motoboy 1 irá realizar: {pedido_m1}'
dados2 = f'O motoboy 2 irá realizar: {pedido_m2}'
dados3 = f'O motoboy 3 irá realizar: {pedido_m3}'
dados4 = f'O motoboy 4 irá realizar: {pedido_m4}'
dados5 = f'O motoboy 5 irá realizar: {pedido_m5}'

m1 = dados1  #atende todas as lojas $ 2 p entrega

m2 =  dados2 #atende todas as lojas $ 2 p entrega

m3 = dados3  # atende todas as lojas $ 2 p entrega

m4 = dados4  # atende somente a loja 1 $ 2 p entrega

m5 = dados5  # atende todas as lojas $ 3 p entrega

relatorio = input('Deseja exibir o relatório do dia: [s]  [n] \n')

if relatorio == 's':
    print('\nRELATÓRIO DO DIA \n')
    print('\n',m1,'\n')
    print(m2,'\n\n')
    print(m3,'\n\n')
    print(m4,'\n\n')
    print(m5,'\n\n')
elif relatorio == 'n':
    print('Até logo')
    
