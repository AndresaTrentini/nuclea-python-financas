import unittest
from unittest.mock import patch
from main import main
from models.ordem import ordens



class TestOrdem(unittest.TestCase):

    def test_ordem(self):
        inputs = ["2", "853.047.920-30", "itau", "itub4", 2.00, 500, "31/07/2023", "5"]

        with patch("builtins.input", side_effect=inputs):
            main()

        ordem_esperada = {
            "nome": "ITAU",
            "ticket": "ITUB4",
            "valor_compra": 2.00,
            "quantidade_compra": 500,
            "data_compra": "31/07/2023",
            "cliente_id": 4

        }

        self.assertIn(ordem_esperada, ordens)

