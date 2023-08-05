from repository.banco_de_dados import BancoDeDados


class Ordem:

    def __init__(self):
        self.id = None
        self.nome = None
        self.ticket = None
        self.valor_compra = None
        self.quantidade_compra = None
        self.data_compra = None
        self.cliente_id = None
        self.banco_de_dados = BancoDeDados()


    def cadastar_ordem(self, ordem):
        self.id = "id"
        self.nome = "nome"
        self.ticket = "ticket"
        self.valor_compra = "valor_compra"
        self.quantidade_compra = "quantidade_compra"
        self.data_compra = "data_compra"
        self.cliente_id = "cliente_id"
        self.banco_de_dados = BancoDeDados()
        self.banco_de_dados.insert(ordem)

        def consultar_ordem(self):
            return self.banco_de_dados.select()

        def alterar_ordem(self, nova_ordem):
            if self.atributos:
                self.banco_de_dados.update(self)
                self.atributos = nova_ordem
                return True
            return False

        def delete_ordem(self):
            if self.atributos:
                self.banco_de_dados.delete(self)
                self.atributos = None
                return True
            return False

    if __name__ == "__main__":
        ordem = Ordem()