'''
while / else
contadores
acumuladores
'''
contador = 1
acumulador = 1

while contador <=5:
     print(contador, acumulador)

     if contador >=4:
         break

     acumulador+= contador
     contador+=1
else:
    print('ADEUS')

print('FIM ')
