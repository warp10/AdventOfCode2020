#!/usr/bin/env python3

import unittest

from solution import get_seat_data, get_seat_id, get_number, main


class TestPuzzle05_2(unittest.TestCase):
    def test_main(self):
        self.assertEqual(get_seat_data('BFFFBBFRRR'), (70, 7))
        self.assertEqual(get_seat_data('FFFBBBFRRR'), (14, 7))
        self.assertEqual(get_seat_data('BBFFBBFRLL'), (102, 4))

        self.assertEqual(get_seat_id(70, 7), 567)
        self.assertEqual(get_seat_id(14, 7), 119)
        self.assertEqual(get_seat_id(102, 4), 820)

        self.assertEqual(main('test_input.txt'), 820)


if __name__ == '__main__':
    unittest.main()
