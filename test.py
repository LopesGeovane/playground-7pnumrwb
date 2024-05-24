import unittest
from solution import soma

class TestSoma(unittest.TestCase):
    def test_soma(self):
        test_cases = [
            (1, 2, 3),
            (-1, 1, 0),
            (0, 0, 0),
            (100, 200, 300)
        ]
        
        for a, b, expected in test_cases:
            result = soma(a, b)
            self.assertEqual(result, expected)
            if result == expected:
                print(f"soma({a}, {b}) = {result} (esperado: {expected})")

if __name__ == '__main__':
    unittest.main()
