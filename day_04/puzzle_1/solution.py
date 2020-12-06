#!/usr/bin/env python3

import re

fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:', ]


def main(filename):
    with open(filename) as f:
        res = f.read().split('\n\n')
        valid_passports = 0
        for line in res:
            keys = re.findall('[a-z]{3}:', line)
            if all(key in keys for key in fields):
                valid_passports += 1
        return valid_passports


if __name__ == '__main__':
    print(main('input.txt'))
