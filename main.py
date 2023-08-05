from models.cliente import Cliente
from relatorio import obter_dados_acao
from utils.cep import valida_cep
from utils.data import valida_data_nascimento
from utils.funcoes_auxiliares import formata_texto,retorna_menu_principal
from utils.valida_cpf import valida_cpf
from utils.valida_rg import valida_rg


def cadastro_cliente():
    print("Informe os dados do cliente: ")
    cliente = {
        "nome": formata_texto(input("Nome: ")),
        "cpf": valida_cpf(),
        "rg": valida_rg(),
        "data_nascimento": valida_data_nascimento(),
        "endereco": valida_cep(),
        "numero_residencia": input("Número casa: ")
    }
    clientes.append(cliente)
    print(clientes)
    novo_cliente = Cliente()
    novo_cliente.cadastrar_cliente(cliente)






def menu_cliente():
    while True:
        print("Menu Cliente")
        print("1 - Cadastrar Cliente")
        print("2 - Consultar Cliente")
        print("3 - Alterar Cliente")
        print("4 - Deletar Cliente")
        print("5 - Retornar Menu Principal")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            cadastro_cliente()
        elif opcao == "2":
            consulta_cliente()
        elif opcao == "3":
            alterar_cliente()
        elif opcao == "4":
            deletar_cliente()
        elif opcao == "5":
            return True
        else:
            print("opcão inválida")






clientes = []


def main():
    validador = True
    while(validador):
        print("Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea. Selecione uma das opções abaixo:")
        print("1 - Cliente")
        print("2 - Ordem")
        print("3 - Realizar análise da carteira")
        print("4 - Imprimir relatório da carteira")
        print("5 - Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            menu_cliente()
        elif opcao == "2":
            cadastrar_ordem()
        elif opcao == "3":
            menu_analise()
        elif opcao == "4":
            ticker = input("Digite o codigo da ação na B3: ").upper().strip()
            nome_arquivo = input("Digite o nome do arquivo de saída: ").strip()
            obter_dados_acao(ticker, nome_arquivo)
        elif opcao == "5":
            print("Obrigado por utilizar o sistema de gerenciamento de carteira de ações da Nuclea. Até a próxima! ")
            validador = False
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

