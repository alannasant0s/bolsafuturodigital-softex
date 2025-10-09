import time

#Este sistema permite adicionar, visualizar, marcar tarefas como concluídas e remover tarefas.

class Tarefa:
    """Representa uma tarefa individual com nome e status."""
    def __init__(self, descricao):
        self.descricao = descricao.strip()
        self.concluida = False
        self.criacao = time.strftime("%Y-%m-%d %H:%M:%S")

    def marcar_como_concluida(self):
        """Muda o status da tarefa para concluída."""
        self.concluida = True

    def __str__(self):
        """Retorna a representação formatada da tarefa."""
        status = "[CONCLUÍDA]" if self.concluida else "[PENDENTE]"
        return f"[{self.criacao}] {status} - {self.descricao}"

class GerenciadorTarefas:
    """Gerencia a coleção de tarefas (a lista de afazeres)."""
    def __init__(self):
        # A lista armazenará objetos da classe Tarefa
        self.lista_tarefas = []
        self.proximo_id = 1

    def adicionar_tarefa(self, descricao):
        """Adiciona uma nova tarefa à lista."""
        if not descricao.strip():
            print("\nERRO: A descrição da tarefa não pode estar vazia.")
            return

        tarefa = Tarefa(descricao)
        # Adiciona um ID para facilitar a manipulação
        setattr(tarefa, 'id', self.proximo_id)
        self.lista_tarefas.append(tarefa)
        self.proximo_id += 1
        print(f"\n✅ Tarefa '{tarefa.descricao}' adicionada com sucesso! (ID: {tarefa.id})")

    def listar_tarefas(self):
        """Exibe todas as tarefas, mostrando ID, status e descrição."""
        if not self.lista_tarefas:
            print("\n--- Sua lista de afazeres está vazia. ---")
            return

        print("\n" + "="*40)
        print("LISTA DE AFAZERES")
        print("="*40)
        
        # Filtra e ordena para mostrar Pendentes primeiro
        pendentes = [t for t in self.lista_tarefas if not t.concluida]
        concluidas = [t for t in self.lista_tarefas if t.concluida]
        
        tarefas_ordenadas = pendentes + concluidas

        for tarefa in tarefas_ordenadas:
            status = "✅" if tarefa.concluida else "⏳"
            print(f"ID: {tarefa.id:<3} {status} {tarefa.descricao} (Criada em: {tarefa.criacao})")

        print("="*40)
    
    def _encontrar_tarefa_por_id(self, id_tarefa):
        """Método auxiliar para localizar uma tarefa pelo ID."""
        try:
            id_busca = int(id_tarefa)
        except ValueError:
            return None
        
        for tarefa in self.lista_tarefas:
            if tarefa.id == id_busca:
                return tarefa
        return None

    def marcar_concluida(self, id_tarefa):
        """Marca uma tarefa como concluída usando seu ID."""
        tarefa = self._encontrar_tarefa_por_id(id_tarefa)
        if tarefa:
            if not tarefa.concluida:
                tarefa.marcar_como_concluida()
                print(f"\n🎉 Tarefa ID {tarefa.id} ('{tarefa.descricao}') marcada como concluída!")
            else:
                print(f"\n⚠️ Tarefa ID {tarefa.id} já estava concluída.")
        else:
            print(f"\nERRO: Tarefa com ID '{id_tarefa}' não encontrada.")

    def remover_tarefa(self, id_tarefa):
        """Remove uma tarefa da lista usando seu ID."""
        tarefa = self._encontrar_tarefa_por_id(id_tarefa)
        if tarefa:
            self.lista_tarefas.remove(tarefa)
            print(f"\n❌ Tarefa ID {tarefa.id} ('{tarefa.descricao}') removida com sucesso.")
        else:
            print(f"\nERRO: Tarefa com ID '{id_tarefa}' não encontrada.")

# --- Funções de Interface do Usuário (CLI) ---

def menu():
    """Exibe o menu de opções."""
    print("\n" + "-"*30)
    print("GERENCIADOR DE TO-DO LIST")
    print("-" * 30)
    print("1. Adicionar nova tarefa")
    print("2. Listar todas as tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Sair")
    print("-" * 30)

def main():
    """Função principal para rodar o sistema."""
    gerenciador = GerenciadorTarefas()

    while True:
        menu()
        escolha = input("Selecione uma opção (1-5): ")

        if escolha == '1':
            descricao = input("Digite a descrição da nova tarefa: ")
            gerenciador.adicionar_tarefa(descricao)
        
        elif escolha == '2':
            gerenciador.listar_tarefas()
        
        elif escolha == '3':
            id_tarefa = input("Digite o ID da tarefa a ser concluída: ")
            gerenciador.marcar_concluida(id_tarefa)

        elif escolha == '4':
            id_tarefa = input("Digite o ID da tarefa a ser removida: ")
            gerenciador.remover_tarefa(id_tarefa)

        elif escolha == '5':
            print("\nEncerrando o Gerenciador de Tarefas. Até logo!")
            break
        
        else:
            print("\nOpção inválida. Por favor, escolha um número de 1 a 5.")

if __name__ == "__main__":
    main()