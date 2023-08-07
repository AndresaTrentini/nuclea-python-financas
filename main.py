from utils.funcoes_auxiliares import retorna_menu_principal
import models.cliente
import models.ordem


def main():
    validador = True
    while validador:
        print("Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea. Selecione uma das opções abaixo:")
        print("1 - Cliente")
        print("2 - Ordem")
        print("3 - Realizar análise da carteira")
        print("4 - Imprimir relatório da carteira")
        print("5 - Sair")

        opcao = input("Digite a opção desejada: ")
        cliente = models.cliente.Cliente()
        ordem = models.ordem.Ordem()

        if opcao == "1":
            print("Menu Cliente")
            print("1 - Cadastrar Cliente")
            print("2 - Consultar Cliente")
            print("3 - Alterar Cliente")
            print("4 - Deletar Cliente")
            print("5 - Retornar Menu Principal")

            opcao = input("Digite a opção desejada: ")

            if opcao == "1":
                cliente.cadastro_cliente()
            elif opcao == "2":
                cliente.consultar_cliente()
            elif opcao == "3":
                cliente.alterar_cliente()
            elif opcao == "4":
                cliente.deletar_cliente()
            elif opcao == "5":
                validador = retorna_menu_principal()
            else:
                print("opcão inválida")
        elif opcao == "2":
            ordem.cadastrar_ordem()
        elif opcao == "3":
            menu_analise_carteira()
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

