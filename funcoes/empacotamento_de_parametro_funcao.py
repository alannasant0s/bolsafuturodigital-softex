def Somatoria(*dados): #significa que esta recebendo parametros empacotados
    r = 0
    for i in dados:
        r+=1
    return r

a = Somatoria(3,5,1)
print(a)