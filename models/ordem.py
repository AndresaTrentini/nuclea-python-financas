from carteira import analise_cliente
from relatorio import obter_dados_carteira, obter_dados_acao
from repository.banco_de_dados import BancoDeDados
from utils.data import valida_data_compra

ordens = []

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


    def cadastrar_ordem(self, ordem):
        self.id = "id"
        self.nome = "nome"
        self.ticket = "ticket"
        self.valor_compra = "valor_compra"
        self.quantidade_compra = "quantidade_compra"
        self.data_compra = "data_compra"
        self.cliente_id = "cliente_id"
        self.banco_de_dados.insert_ordem_bdd(ordem)

    def consultar_ordem(self, cliente):
        carteira_selecionada = self.banco_de_dados.select_ordem_bdd(cliente)
        return carteira_selecionada

    def cadastro_ordem(self, cliente):
        print("[2] - Módulo Cadastro de Ordem/Ações - Informe seu cpf para acessar o sistema: ")
        cliente_encontrado = cliente.consultar_cliente()
        if cliente_encontrado is not None:
            ordem = {
                'nome': input("Digite o nome da ação: ").upper(),
                'ticket': input("Digite ticker da ação").upper(),
                'valor_compra': float(input("Digite o valor de compra: ")),
                'quantidade_compra': int(input("Digite a quantidade: ")),
                'data_compra': valida_data_compra(),
                'cliente_id': cliente_encontrado['id']
            }
            self.cadastrar_ordem(ordem)
            ordens.append(ordem)
            print("Ordem finalizada com sucesso")
        else:
            print("Documento não encontrado")

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

    def analise_carteira(self, cliente):
        print("[3] - Analise da Carteira")
        cliente_encontrado = cliente.consultar_cliente()
        if cliente_encontrado is not None:
            carteira_cliente = self.banco_de_dados.select_ordem_bdd(cliente_encontrado["id"])
            if carteira_cliente is not None:
                data_inicio = input("Informe a Data de inicio no formato: YYYY-MM-dd ")
                data_fim = input("Informe a Data de final no formato: YYYY-MM-dd ")
                analise_cliente(carteira_cliente, data_inicio, data_fim)

    def imprimir_relatorio_carteira(self, cliente):
        print("[1] - Imprimir relatorio da carteira")
        cliente_encontrado = cliente.consultar_cliente()
        if cliente_encontrado is not None:
            carteira_cliente = self.banco_de_dados.select_ordem_bdd(cliente_encontrado["id"])
            if carteira_cliente is not None:
                nome_arquivo = input("Digite nome do arquivo de saída ").strip()
                obter_dados_carteira(carteira_cliente, nome_arquivo)
            else:
                print("Não constam ações neste documento")
        else:
            print("Documento não encontrado")

    @staticmethod
    def imprime_relatorio():
        print("2 - Imprimir relatorio ação")
        ticket = input("Informe o ticket a ser consultado: ")
        nome_arquivo = input("Digite nome do arquivo de saída ").strip()
        obter_dados_acao(ticket, nome_arquivo)



