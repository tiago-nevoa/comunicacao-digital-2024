import unittest
from information_theory import informational_value, entropy

class TestFunctions(unittest.TestCase):

    def test_informational_value(self):
        self.assertEqual(informational_value('A', {'A': 0.5, 'B': 0.5}), 1.0)
        self.assertEqual(informational_value('A', {'A': 0.25, 'B': 0.5, 'C': 0.25}), 2.0)

        with self.assertRaises(ValueError):
            informational_value('b', {'A': 0.25, 'B': 0.5})

    def test_entropy(self):
        self.assertEqual(entropy({'A': 0.5, 'B': 0.5}), 1.0)


if __name__ == '__main__':
    unittest.main()