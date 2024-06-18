# pysphere/tests/test_char_functions.py

import unittest
from src.char_functions import CChar

class TestCCharFunctions(unittest.TestCase):
    def setUp(self):
        self.char = CChar()

    def test_afk(self):
        self.char.afk()
        # Podemos adicionar asserções específicas se as funções tiverem retornos ou efeitos colaterais

    def test_allskills(self):
        self.char.allskills()

    # Adicionar mais testes conforme necessário para todas as funções...

if __name__ == '__main__':
    unittest.main()

