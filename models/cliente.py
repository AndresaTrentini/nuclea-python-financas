from repository.banco_de_dados import BancoDeDados


class Cliente:

    def __init__(self):
        self.cpf = None
        self.id = None
        self.nome = None
        self.rg = None
        self.data_nascimento = None
        self.cep = None
        self.logradouro = None
        self.numero_residencia = None
        self.bairro = None
        self.cidade = None
        self.estado = None
        self.banco_de_dados = BancoDeDados()

    def cadastrar_cliente(self, cliente):
        self.cpf = "cpf"
        self.id = "id"
        self.nome = "nome"
        self.rg = "rg"
        self.data_nascimento = "data_nascimento"
        self.cep = "cep"
        self.logradouro = "logradouro"
        self.numero_residencia = "numero_residencia"
        self.bairro = "bairro"
        self.cidade = "cidade"
        self.estado = "estado"
        self.banco_de_dados.insert(cliente)
    def consultar_cliente(self):
        return self.banco_de_dados.select()

    def alterar_cliente(self, cliente_atualizado):
        if self.cpf:
            self.banco_de_dados.update(self)
            self.cpf = cliente_atualizado
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