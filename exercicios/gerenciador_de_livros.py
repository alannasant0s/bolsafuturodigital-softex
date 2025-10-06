class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.lido = False

    def marcar_como_lido(self):
        self.lido = True

    def exibir_status(self):
        if self.lido:
            status = "Já foi lido"
        else:
            status = "Ainda não foi lido"
              
        print(f"O livro {self.titulo}, de {self.autor}, {status}.")      

print("Criando o livro...")

livro1 = Livro("A Arte da Guerra", "Sun Tzu")
livro2 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry")

##Chamando o método para marcar como lido

livro1.marcar_como_lido()
livro1.exibir_status()
livro2.exibir_status()
