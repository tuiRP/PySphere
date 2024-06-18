# pysphere/tests/test_base_base_def_props.py

import unittest
from src.base_base_def_props import CBaseBaseDef

class TestCBaseBaseDef(unittest.TestCase):
    def test_get_attribute(self):
        self.assertEqual(CBaseBaseDef.get_attribute("ABILITYPRIMARY"), "ABILITYPRIMARY")
        self.assertEqual(CBaseBaseDef.get_attribute("ARMOR"), "ARMOR")
        self.assertIsNone(CBaseBaseDef.get_attribute("NON_EXISTENT"))

if __name__ == '__main__':
    unittest.main()

