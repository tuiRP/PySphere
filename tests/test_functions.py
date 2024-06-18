# pysphere/tests/test_functions.py

import unittest
from src.functions import calculate_damage

class TestFunctions(unittest.TestCase):
    def test_calculate_damage(self):
        self.assertEqual(calculate_damage(10, 5), 50)
        self.assertEqual(calculate_damage(0, 5), 0)
        self.assertEqual(calculate_damage(10, 0), 0)
        self.assertEqual(calculate_damage(-10, 5), -50)

if __name__ == '__main__':
    unittest.main()

