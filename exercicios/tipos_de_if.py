Codigos = [103, 117, 121, 135, 161, 189, 208, 284, 216]
Lista =[]

print(" Utilizando if clássico ")
for codigo in Codigos:
    if 120 <= codigo and codigo <= 200:
        Lista.append(codigo)
print(f" ----Códigos filtrados---- {Lista}")


lista = []
print("\n\n----Utilizando if inline----")
for codigo in Codigos:
    Lista.append(codigo) if 120 <= codigo and codigo <= 200 else 0

print(f" ----Códigos filtrados---- {Lista}")