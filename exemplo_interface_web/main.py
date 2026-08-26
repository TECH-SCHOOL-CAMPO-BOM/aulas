class Tarefa:
    def __init__(self, titulo):
        self.titulo = titulo
        self.concluida = False

    def concluir(self):
        self.concluida = True


class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar(self, titulo):
        nova_tarefa = Tarefa(titulo)
        self.tarefas.append(nova_tarefa)

    def listar(self):
        return self.tarefas

    def concluir(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].concluir()
            return True
        return False
