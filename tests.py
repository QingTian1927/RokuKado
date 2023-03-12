import unittest

from card_validation import get_card_type
from card_validation import compare_played_cards

class TestCardValidation(unittest.TestCase):
    def test_quad(self):
        data = ('4') * 4
        expected = 'quadtuple'
        results = get_card_type(data)
        self.assertEqual(results, expected, f"{results=}")

    def test_single(self):
        data = 'A'
        expected = 'single'
        results = get_card_type(data)
        self.assertEqual(results, expected, f"{results=}")

    def test_equalizer(self):
        data = ('3', '3', '4', '4', '5', '5')
        expected = 'equalizer'
        results = get_card_type(data)
        self.assertEqual(results, expected, f"{results=}")

    def test_alldouble(self):
        data = ('3', '3', '5', '5', '7', '7', '10', '10', 'A', 'A')
        expected = 'all_double'
        results = get_card_type(data)
        self.assertEqual(results, expected, f"{results=}")

    def test_series(self):
        data = ('3', '4', '5', '6')
        expected = 'series'
        results = get_card_type(data)
        self.assertEqual(results, expected, f"{results=}")


class TestCardComparison(unittest.TestCase):
    def test_triple(self):
        results = compare_played_cards(('4', '4', '4'), ('6', '6', '6'))
        expected = True
        self.assertEqual(results, expected, f"{results=}")

    def test_double(self):
        results = compare_played_cards(('J', 'J'), ('A', 'A'))
        expected = True
        self.assertEqual(results, expected, f"{results=}")

    def test_quad(self):
        results = compare_played_cards(('2'), ('6', '6', '6', '6'))
        expected = True
        self.assertEqual(results, expected, f"{results=}")

    def test_equalizer(self):
        results = compare_played_cards(('2'), ('3', '3', '4', '4', '5', '5'))
        expected = True
        self.assertEqual(results, expected, f"{results=}")

    def test_series(self):
        results = compare_played_cards(('3', '4', '5', '6'), ('J', 'Q', 'K', 'A'))
        expected = True
        self.assertEqual(results, expected, f"{results=}")


if __name__ == '__main__':
    unittest.main(verbosity=2)

