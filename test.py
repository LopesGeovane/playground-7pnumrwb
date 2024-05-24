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
        
        results = []
        for a, b, expected in test_cases:
            result = soma(a, b)
            results.append(f"soma({a}, {b}) = {result} (esperado: {expected})")
            self.assertEqual(result, expected)
        
        for r in results:
            print(r)

if __name__ == '__main__':
    unittest.main()
