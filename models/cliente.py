from repository.banco_de_dados import BancoDeDados
from utils.cep import valida_cep
from utils.data import valida_data_nascimento
from utils.funcoes_auxiliares import formata_texto
from utils.valida_cpf import valida_cpf
from utils.valida_rg import valida_rg

clientes = []


class Cliente:
    def __init__(self):
        self.id = None
        self.cpf = None
        self.nome = None
        self.rg = None
        self.data_nascimento = None
        self.cep = None
        self.logradouro = None
        self.numero_residencia = None
        self.bairro = None
        self.cidade = None
        self.estado = None
        self.complemento = None
        self.banco_de_dados = BancoDeDados()

    def cadastrar_cliente(self, cliente):
        self.id = "id"
        self.nome = "nome"
        self.cpf = "cpf"
        self.rg = "rg"
        self.data_nascimento = "data_nascimento"
        self.cep = "cep"
        self.logradouro = "logradouro"
        self.numero_residencia = "numero_residencia"
        self.complemento = "complemento"
        self.bairro = "bairro"
        self.cidade = "cidade"
        self.estado = "estado"
        self.banco_de_dados.insert(cliente)

    def cadastro_cliente(self):
        print("Informe os dados do cliente: ")
        cliente = {
            "nome": formata_texto(input("Nome: ")),
            "cpf": valida_cpf(),
            "rg": valida_rg(),
            "data_nascimento": valida_data_nascimento(),
            "endereco": valida_cep(),
            "numero_residencia": input("Número casa: ")
        }
        self.cadastrar_cliente(cliente)
        clientes.append(cliente)
        print(cliente)

    def consultar_cliente(self):
        cpf = input("Digite seu cpf :")
        cliente_encontrado = self.banco_de_dados.select(cpf)
        if cliente_encontrado is not None:
            return cpf, self
        else:
            print("Documento não encontrado")

    def alterar_cliente(self):
        cpf = input("Digite o CPF do cliente a ser atualizado: ")
        print("Informe os dados do cliente: ")
        cliente_novo = {
            "nome": formata_texto(input("Nome: ")),
            "cpf": valida_cpf(),
            "rg": valida_rg(),
            "data_nascimento": valida_data_nascimento(),
            "endereco": valida_cep(),
            "numero_residencia": input("Número casa: ")
        }
        self.banco_de_dados.update(cpf, cliente_novo)

    def deletar_cliente(self):
        cpf = input("Digite o CPF do cliente a ser deletado: ")
        self.banco_de_dados.delete(cpf)
