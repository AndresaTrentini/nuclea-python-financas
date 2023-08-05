import unittest
from unittest.mock import patch
from main import main



class TestOrdem(unittest.TestCase):

    def test_ordem(self):
        inputs = ["2", "itau", "itub4", 2.00, 500, "31/07/2023", 2, "nao"]

        with patch("builtins.input", side_effect=inputs):
            main()

        ordem_esperada = {
            "nome": "nome",
            "ticket": "ticket",
            "valor_compra": 2.00,
            "quantidade_compra": 500,
            "data_compra": "31/07/2023",
            "cliente_id": 2

        }

        # self.assertIn(ordem_esperada, ordem)

