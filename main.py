from utils.cep import valida_cep
from utils.data import valida_data_nascimento
from utils.funcoes_auxiliares import formata_texto,retorna_menu_principal
from utils.valida_cpf import valida_cpf
from utils.valida_rg import valida_rg


clientes = []

def main():
    validador = True
    while(validador):
        print("Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea. Selecione uma das opções abaixo:")
        print("1 - cliente")
        #Deve alterar o "Cadastrar cliente" por "Cliente"  e exibir submenu com as devidas opções do CRUD.
        print("2 - Ordem")
        print("3 - Realizar análise da carteira")
        print("4 - Imprimir relatório da carteira")
        print("5 - Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            print("Informe os dados do cliente: ")
            cliente = {
                "nome": formata_texto(input("Nome: ")),
                "cpf": valida_cpf(),
                "rg": valida_rg(),
                "data_nascimento": valida_data_nascimento(),
                "endereco": valida_cep(),
                "numero_casa": input("Número casa: ")
            }
            clientes.append(cliente)
            print(clientes)
            #Corrigir o validador para evitar duplicidade do retorna_menu_principal
            validador = retorna_menu_principal()

        elif opcao == "2":
            pass
            #Preencher a função da ordem.
        elif opcao == "3":
            pass
        elif opcao == "4":
            pass
        elif opcao == "5":
            print("Obrigado por utilizar o sistema de gerenciamento de carteira de ações da Nuclea. Até a próxima!")
            validador = False
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

