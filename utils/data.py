from datetime import datetime


def valida_data_nascimento():

    while True:
        data_nascimento = input("Data Nascimento: ")
        try:
            data_convertida = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
            data_atual = datetime.now().date()

            if data_convertida < data_atual:
                return data_convertida.strftime("%d/%m/%Y")
            else:
                print("A data de nascimento não pode ser maior que a data atual.")
        except ValueError as e:
            print("Recebei um erro: ", e ,", porém estou utilizando tratamento de erros. Digite novamente a data de nascimento.")


def valida_data_compra():

    while True:
        data_compra = input("Data Compra: ")
        try:
            data_convertida = datetime.strptime(data_compra, "%d/%m/%Y").date()
            data_atual = datetime.now().date()

            if data_convertida <= data_atual:
                return data_convertida.strftime("%d/%m/%Y")
            else:
                print("A data de compra não pode ser maior que a data atual.")
        except ValueError as e:
            print("Recebei um erro: ", e ,", porém estou utilizando tratamento de erros. Digite novamente a data de compra.")




if __name__ == "__main__":
    valida_data()



