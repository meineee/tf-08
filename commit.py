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
