import unittest
from arithmetic_progression import arithmetic_progression
from fatorial import fatorial
from mmc import mmc
from primes_in_range import primes_in_range
from symbol_frequency import *

files = ["guia_pratico/TestFiles/something.txt",
            "modulo_1/TestFiles/CD/a.txt",
            "modulo_1/TestFiles/CD/alice29.txt",
            "modulo_1/TestFiles/CD/arrays.kt"]

class TestFunctions(unittest.TestCase):

    def test_arithmetic_progression(self):
        self.assertEqual(arithmetic_progression(5, 1, 2), [1, 3, 5, 7, 9])
        self.assertEqual(arithmetic_progression(6, -4, 2), [-4, -2, 0, 2, 4, 6])
        self.assertEqual(arithmetic_progression(3, 2, 0), [2, 2, 2])
        self.assertEqual(arithmetic_progression(5, 5, -3), [5, 2, -1, -4, -7])

        with self.assertRaises(ValueError):
            arithmetic_progression(0, 1, 2)
            arithmetic_progression(-1, 1, 2)

    def test_fatorial(self):
        self.assertEqual(fatorial(0), 1)
        self.assertEqual(fatorial(1), 1)
        self.assertEqual(fatorial(2), 2)
        self.assertEqual(fatorial(5), 120)
        self.assertEqual(fatorial(5.5), 324.84375)

        with self.assertRaises(ValueError):
            fatorial(-1)
            fatorial(-2)
            fatorial("12")

    def test_mmc(self):
        self.assertEqual(mmc(6, 12), 12)
        self.assertEqual(mmc(24, 60), 120)
        self.assertEqual(mmc(-2, 4), 4)
        self.assertEqual(mmc(-40, -10), 40)

        with self.assertRaises(ValueError):
            mmc(0, 0)
            mmc(6, 0)
            mmc(0, 12)

    def test_primes_in_range(self):
        self.assertEqual(primes_in_range(0, 19), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(primes_in_range(-4, 7), [2, 3, 5, 7])
        self.assertEqual(primes_in_range(7, 7), [7])
        self.assertEqual(primes_in_range(14, 16), [])

        with self.assertRaises(ValueError):
            primes_in_range(19, 15)
            primes_in_range(0, -5)
            primes_in_range(-3, -10)
        
    def test_file_symb_freq(self):
        self.assertEqual(file_symb_freq(files[0], 1), {'A': 12, 'B': 1, 'C': 4, 'F': 6, 'G': 4})


    # Test for Auxilary Functions
        
    def test_get_symbol_frequencies(self):
        self.assertEqual(get_symbol_frequencies("AABB"), {'A': 2, 'B': 2})
        self.assertEqual(get_symbol_frequencies("AAABd 5"), {' ': 1, '5': 1, 'A': 3, 'B': 1, 'd': 1})

        with self.assertRaises(ValueError):
            get_symbol_frequencies(21)

    def test_filter_frequencies(self):
        self.assertEqual(filter_frequencies({'H': 2, 'A': 1, 'D': 4}, 7, 50), {'D': 4})

    def test_sort_frequencies(self):
        self.assertEqual(sort_frequencies({'H': 2, 'A': 1, 'D': 4}), {'A': 1, 'D': 4, 'H': 2})

    def test_get_symbol_probabilities(self):
        self.assertEqual(get_symbol_probabilities("AB"), {'A': 0.5, 'B': 0.5})
        self.assertEqual(get_symbol_probabilities("AB", True), {'A': 50, 'B': 50})
        self.assertEqual(get_symbol_probabilities("ABBB"), {'A': 0.25, 'B': 0.75})
        self.assertEqual(get_symbol_probabilities("AbCC"), {'A': 0.25, 'b': 0.25, 'C': 0.5})
        self.assertEqual(get_symbol_probabilities("AbCC", True), {'A': 25, 'b': 25, 'C': 50})

        with self.assertRaises(ValueError):
            get_symbol_probabilities(11)
            get_symbol_probabilities(False)

    def test_most_probable_symbols(self):
        self.assertEqual(most_probable_symbols({'A': 0.5, 'B': 0.25, 'C': 0.25}, 1), ['A'])
        self.assertEqual(most_probable_symbols({'B': 0.25, 'A': 0.25}, 1), ['B'])
        self.assertEqual(most_probable_symbols({'A': 0.25, 'B': 0.75}, 1), ['B'])
        self.assertEqual(most_probable_symbols({'A': 0.25, 'B': 0.75}, 2), ['B', 'A'])
        self.assertEqual(most_probable_symbols({'O': 0.12, 'h': 0.31, 'b': 0.04, 'Q': 0.53}, 2), ['Q', 'h'])

    def test_sort_probabilities(self):
        self.assertEqual(sort_probabilities({'O': 0.12, 'h': 0.31, 'b': 0.04, 'Q': 0.53}), {'Q': 0.53, 'h': 0.31, 'O': 0.12, 'b': 0.04})


if __name__ == '__main__':
    unittest.main()