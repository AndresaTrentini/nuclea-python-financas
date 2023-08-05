import psycopg2
import os


# CLASSE:
# FORMA DE BOLO, ESTEIRA DE PRODUÇÃO DE UM VEICULO;
# ATRIBUTO/CARICTERISTICA;
# CHASSI, COR, QUANTIDADE DE PORTAS, POTENCIA MOTOR, CAMBIO;
# METODOS/FUNCOES:
# ACOES, COMPORTAMENTO, 4X4, TURBO, ANDAR, ESTACIONAR, TROCAR DE MARCHA
# __init__
# Construcao do objeto
# __del__
# Delecao do objeto

# java objeto = new Class();
# python objeto = Class()

# variavel = cliente
# funcao = cliente()
# classe = Cliente()

class BancoDeDados:

    def __init__(self):
        self.connection = psycopg2.connect(**self.retorna_parametros_conexao_banco_de_dados())
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def insert(self, cliente):
        print("Inserindo cliente no banco de dados: ")
        insert_query = """
                INSERT INTO cliente (nome, cpf, rg, data_nascimento, cep, logradouro, complemento,
	            bairro, cidade, estado, numero_residencia)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                """
        values = (
            cliente['nome'],
            cliente['cpf'],
            cliente['rg'],
            cliente['data_nascimento'],
            cliente['cep']['Cep'],
            cliente['cep']['logradouro'],
            cliente['cep']['complemento'],
            cliente['cep']['bairro'],
            cliente['cep']['cidade'],
            cliente['cep']['estado'],
            cliente['numero_residencia']
        )
        self.cursor.execute(insert_query, values)
        self.connection.commit()

    def select(self, cliente):
        print("Selecionando cliente no banco de dados: ")
        select_query = "SELECT * FROM CLIENTE where cpf = '" + cliente['cpf'] + "';"
        self.cursor.execute(select_query)
        clientes = self.cursor.fetchall()
        for cliente in clientes:
            print(cliente)
        return clientes
    def delete(self, cliente):
        print("Deletando cliente no banco de dados")
        delete_query = "DELETE * FROM CLIENTE where cpf = '" + cliente['cpf'] + "';"
        self.cursor.execute(delete_query)
        self.connection.commit()


    def update(self, cliente):
        print("Atualizando cliente no banco de dados: ")
        update_query = """
            UPDATE cliente 
            SET nome = %s,
                rg = %s,
                data_nascimento = %s,
                cep = %s,
                logradouro = %s,
                complemento = %s,
                bairro = %s,
                cidade = %s,
                estado = %s,
                numero_residencia = %s
            WHERE cpf = %s;
        """
        values = (
            cliente['nome'],
            cliente['rg'],
            cliente['data_nascimento'],
            cliente['cep']['CEP'],
            cliente['cep']['logradouro'],
            cliente['cep']['complemento'],
            cliente['cep']['bairro'],
            cliente['cep']['cidade'],
            cliente['cep']['estado'],
            cliente['numero_residencia'],
            cliente['cpf']
        )
        self.cursor.execute(update_query, values)
        self.connection.commit()


    @staticmethod
    def retorna_parametros_conexao_banco_de_dados():
        parametros_conexao = {
            "user": os.getenv('user'),
            "password": os.getenv('password'),
            "host": os.getenv('host'),
            "port": os.getenv('port'),
            "database": os.getenv('database')
        }

        return parametros_conexao



# Realizar integração com a classe cliente.
conexao = BancoDeDados()
