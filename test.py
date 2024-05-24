import unittest
from solution import soma

class TestSoma(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(1, 2), 3)
        self.assertEqual(soma(-1, 1), 0)
        self.assertEqual(soma(0, 0), 0)
        self.assertEqual(soma(100, 200), 300)

if __name__ == '__main__':
    unittest.main()
