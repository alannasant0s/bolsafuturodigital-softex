class Passaro:
 def voar(self):
    return "O pássaro está voando no céu."
class Gato:
 def voar(self):
 # O método tem o mesmo nome, mas comportamento diferente (ou inexistente)
    return "O gato não voa, está pulando no sofá."
class Aviao:
 def voar(self):
    return "O avião está decolando e voando muito alto."
# Objetos
pipoca = Passaro()
miau = Gato()
boeing = Aviao()
# Ação: Chamando o mesmo método 'voar()' em objetos diferentes
print("\n--- Polimorfismo ---")
for objeto in [pipoca, miau, boeing]:
 # O resultado (a forma) é diferente, mas o comando (o método) é o mesmo
 print(objeto.voar())