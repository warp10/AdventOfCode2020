#!/usr/bin/env python3

import unittest

from solution import main


class TestPuzzle10_2(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main('test_input_1.txt'), 8)
        self.assertEqual(main('test_input_2.txt'), 19208)


if __name__ == '__main__':
    unittest.main()
