from utils.funcoes_auxiliares import retorna_menu_principal
import models.cliente
import models.ordem


def main():
    validador = True
    while validador:
        print(
            "Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea. Selecione uma das opções abaixo:")
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
            ordem.cadastro_ordem(cliente)
        elif opcao == "3":
            ordem.analise_carteira(cliente)
        elif opcao == "4":
            print("Menu relatório carteira")
            print("1 - Imprimir relatório carteira")
            print("2 - Imprimir relatório ação")
            print("3 - Retornar ao menu principal")

            opcao = input("Digite a opção desejada: ")

            if opcao == "1":
                ordem.imprimir_relatorio_carteira(cliente)
            elif opcao == "2":
                ordem.imprime_relatorio()
            elif opcao == "3":
                validador = retorna_menu_principal()
            else:
                print("opção inválida")


        elif opcao == "5":
            print("Obrigado por utilizar o sistema de gerenciamento de carteira de ações da Nuclea. Até a próxima! ")
            validador = False
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
