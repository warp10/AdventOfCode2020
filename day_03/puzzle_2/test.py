#!/usr/bin/env python3

import unittest

from solution import main


class TestPuzzle03_2(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main('test_input.txt', 2, 0), 2)
        self.assertEqual(main('test_input.txt', 4, 0), 7)
        self.assertEqual(main('test_input.txt', 6, 0), 3)
        self.assertEqual(main('test_input.txt', 8, 0), 4)
        self.assertEqual(main('test_input.txt', 2, 1), 2)


if __name__ == '__main__':
    unittest.main()
