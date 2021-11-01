contador_progressivo = 0
contador_regressivo = 10

for p, r in enumerate(range(10 , 1, -1)):
    print(p , r)

print('-----------')

while True:
    if contador_progressivo >= 0 and contador_progressivo <=8 or contador_regressivo <= 10 and contador_regressivo >=2:
        print(contador_progressivo, contador_regressivo)
        contador_progressivo +=1
        contador_regressivo -=1
    