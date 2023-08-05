from repository.banco_de_dados import BancoDeDados


class Cliente:

    def __init__(self):
        self.cpf = None
        self.banco_de_dados = BancoDeDados()

    def cadastrar_cliente(self):
        self.cpf = "cpf"
        self.banco_de_dados.insert()
    def consultar_cliente(self):
        return self.banco_de_dados.select()

    def alterar_cliente(self, novo_cadastro):
        if self.cpf:
            self.banco_de_dados.update(self)
            self.cpf = novo_cadastro
            return True
        return False

    def delete_cliente(self):
        if self.cpf:
            self.banco_de_dados.delete(self)
            self.cpf = None
            return True
        return False

if __name__ == "__main__":
 cliente = Cliente()