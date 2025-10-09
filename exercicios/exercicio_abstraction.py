class Impressora:
 def __init__(self, modelo):
    self.modelo = modelo
 # Complexidade interna que não será exposta
    self.__status_hardware = "Aguardando"

 def __preparar_documento(self, documento):
 # Método interno complexo (abstraído)
    return f"({self.modelo}) Preparando {documento} para conversão de formato..."

 # Método Público (Abstração): O único que o usuário precisa
def imprimir(self, documento):
    preparo = self.__preparar_documento(documento)
    print(preparo)
    print(f"Enviando dados para o chip de impressão...")
    return f"Documento '{documento}' impresso com sucesso!"
# Objeto
impressora_laser = Impressora(modelo="LaserJet P20")
# Ação
print("\n--- Abstração ---")
# O usuário só precisa chamar 'imprimir()', o método interno '__preparar_documento' está escondido
print(impressora_laser.imprimir("Relatório Final.pdf"))