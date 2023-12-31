import psycopg2
import os


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
            cliente['endereco']['CEP'],
            cliente['endereco']['Logradouro'],
            cliente['endereco']['Complemento'],
            cliente['endereco']['Bairro'],
            cliente['endereco']['Cidade'],
            cliente['endereco']['Estado'],
            cliente['numero_residencia']
            )
        self.cursor.execute(insert_query, values)
        self.connection.commit()

    def select(self, cpf):
        print("Selecionando cliente no banco de dados: ")
        select_query = "SELECT * FROM CLIENTE where cpf = '" + cpf + "';"
        self.cursor.execute(select_query)
        linha = self.cursor.fetchone()
        if linha:
            coluna = [dado[0]for dado in self.cursor.description]
            select_chave_valores = (dict(zip(coluna, linha)))
            print(linha)
            return select_chave_valores

    def delete(self, cpf):
        print("Deletando cliente no banco de dados")
        delete_query = "DELETE FROM CLIENTE where cpf = '" + cpf + "';"
        self.cursor.execute(delete_query)
        self.connection.commit()

    def update(self, cpf, cliente_novo):
        print("Atualizando cliente no banco de dados: ")
        update_query = """
                    UPDATE cliente
                    SET nome = %s, cpf = %s, rg = %s, data_nascimento = %s,
                        cep = %s, logradouro = %s, numero_residencia = %s, complemento = %s,
                        bairro = %s, cidade = %s, estado = %s
                    WHERE cpf = %s;
                """
        values = (
            cliente_novo['nome'],
            cliente_novo['cpf'],
            cliente_novo['rg'],
            cliente_novo['data_nascimento'],
            cliente_novo['endereco']['CEP'],
            cliente_novo['endereco']['Logradouro'],
            cliente_novo['endereco']['Complemento'],
            cliente_novo['endereco']['Bairro'],
            cliente_novo['endereco']['Cidade'],
            cliente_novo['endereco']['Estado'],
            cliente_novo['numero_residencia'],
            cpf
        )
        self.cursor.execute(update_query, values)
        self.connection.commit()

    def insert_ordem_bdd(self, ordem):
        print("Inserindo cliente no banco de dados: ")
        insert_query = """
                   INSERT INTO ordem (nome, ticket, valor_compra, quantidade_compra, data_compra, cliente_id)
                   VALUES (%s, %s, %s, %s, %s, %s);
                   """
        values = (
            ordem['nome'],
            ordem['ticket'],
            ordem['valor_compra'],
            ordem['quantidade_compra'],
            ordem['data_compra'],
            ordem['cliente_id']
        )
        self.cursor.execute(insert_query, values)
        self.connection.commit()

    def select_ordem_bdd(self, cliente_id):
        print("Buscando carteira no banco de dados")
        select_query = f"SELECT * FROM ORDEM where cliente_id = {cliente_id}"
        self.cursor.execute(select_query)
        linhas = self.cursor.fetchall()
        if linhas:
            coluna = [dado[0] for dado in self.cursor.description]
            resultado = []
            for linha in linhas:
                resultado_dicionario = dict(zip(coluna, linha))
                resultado.append(resultado_dicionario)
            return resultado



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
