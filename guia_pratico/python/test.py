import unittest
from arithmetic_progression import arithmetic_progression
from fatorial import fatorial
from mmc import mmc
from primes_in_range import primes_in_range
from symbol_frequency import file_symb_freq, symb_frequencies


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

        with self.assertRaises(ValueError):
            fatorial(-1)
            fatorial(-2)

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

    def test_symb_frequencies(self):
        self.assertEqual(symb_frequencies("AABB"), {'A': 2, 'B': 2})
        self.assertEqual(symb_frequencies("AAABd 5"), {' ': 1, '5': 1, 'A': 3, 'B': 1, 'd': 1})

        with self.assertRaises(ValueError):
            symb_frequencies(21)
        
    def test_file_symb_freq(self):
        self.assertEqual(file_symb_freq("guia-pratico/TestFiles/something.txt", 1), {'A': 12, 'B': 1, 'C': 4, 'F': 6, 'G': 4})



if __name__ == '__main__':
    unittest.main()