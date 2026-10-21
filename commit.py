class Commit:
    def __init__(self, id, mensagem, autor, pai = None):
        self.id = id
        self.mensagem = mensagem
        self.autor = autor
        self.pai = pai

    def historico(self):
        print(f"#{self.id} {self.mensagem} ({self.autor})")
        if self.pai is not None:
            self.pai.historico()


class Repositorio:
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor
        self.head = None
        self.contador_de_commits = 0

    def commitar(self, mensagem):
        self.contador_de_commits += 1
        self.head = Commit(
            self.contador_de_commits,
            mensagem,
            self.autor,
            self.head,
        )

    def log(self):
        if self.head is None:
            print("Nenhum commit ainda")
        else:
            self.head.historico()

    def total_de_commits(self):
        total = 0
        commit = self.head
        while commit is not None:
            total += 1
            commit = commit.pai
        return total
