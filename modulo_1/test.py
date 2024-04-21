import unittest
from information_theory import get_informational_value, get_entropy

class TestFunctions(unittest.TestCase):

    def test_informational_value(self):
        self.assertEqual(get_informational_value('A', {'A': 0.5, 'B': 0.5}), 1.0)
        self.assertEqual(get_informational_value('A', {'A': 0.25, 'B': 0.5, 'C': 0.25}), 2.0)

        with self.assertRaises(ValueError):
            get_informational_value('b', {'A': 0.25, 'B': 0.5})

    def test_entropy(self):
        self.assertEqual(get_entropy({'A': 0.5, 'B': 0.5}), 1.0)


if __name__ == '__main__':
    unittest.main()