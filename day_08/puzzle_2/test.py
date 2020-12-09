#!/usr/bin/env python3

import unittest

from solution import main


class TestPuzzle08_2(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main('test_input.txt'), 8)


if __name__ == '__main__':
    unittest.main()
