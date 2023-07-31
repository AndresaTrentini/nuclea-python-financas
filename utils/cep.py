import requests

def busca_cep(cep):
    url = f"http://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "erro" not in data:
            endereco = {
                "CEP": data['cep'],
                "Logradouro": data['logradouro'],
                "Complemento": data['complemento'],
                "Bairro": data['bairro'],
                "Cidade": data['localidade'],
                "Estado": data['uf']
            }

            return endereco


def valida_cep():
    print("Consulta do CEP - ViaCEP")

    while True:
        cep_input = input("CEP: ")

        if cep_input.isdigit() and len(cep_input) == 8:
            retorno_cep = busca_cep(cep_input)
            if retorno_cep:
                return retorno_cep
            else:
                print("CEP não encontrado ou inválido.")



if __name__ == "__main__":
    valida_cep()



# from requests import get
#
# def get_endereco(numero):
#     url = f"http://viacep.com.br/ws/{numero}/json/"
#     try:
#         response = get(url)
#         local = response.json()
#         endereco = local['logradouro']+" - "+local['bairro']+"/"+local['uf']
#         return endereco
#     except:
#         return "CEP inválido"
#
# print(get_endereco('60830035')) # Rua Elizeu Oriá - José de Alencar/CE
# print(get_endereco('60830036')) # CEP inválido
#
# if __name__ == "__main__":
#  get_endereco("01310930")
# # var = 'False'