#!/usr/bin/env python3

import unittest

from solution import main


class TestPuzzle09_1(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main('test_input_1.txt'), 35)
        self.assertEqual(main('test_input_2.txt'), 220)


if __name__ == '__main__':
    unittest.main()
