# Superclasse (Classe Mãe)
class Animal:
 def __init__(self, nome, especie):
    self.nome = nome
    self.especie = especie

 def comer(self):
    return f"{self.nome} está comendo."

# Subclasse (Classe Filha) que herda de Animal
class Cachorro(Animal):
 def __init__(self, nome, raca):
 # Chama o construtor da classe mãe
    super().__init__(nome, especie="Canino")
    self.raca = raca

 def latir(self):
    return f"{self.nome}, da raça {self.raca}, está latindo: Au au!"
# Objeto
meu_cachorro = Cachorro(nome="Rex", raca="Labrador")
# Ação
print("\n--- Herança ---")
# O método 'comer' foi herdado da classe Animal
print(meu_cachorro.comer())
# O atributo 'especie' foi definido na classe mãe
print(f"Espécie: {meu_cachorro.especie}")
# O método 'latir' é exclusivo da subclasse
print(meu_cachorro.latir())