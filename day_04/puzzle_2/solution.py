#!/usr/bin/env python3

import string
import re


def validator_byr(value):
    return 1920 <= int(value) <= 2002


def validator_iyr(value):
    return 2010 <= int(value) <= 2020


def validator_eyr(value):
    return 2020 <= int(value) <= 2030


def validator_hgt(value):
    try:
        uom = value[-2:]
        measure = int(value[:-2])
        if uom == 'cm':
            return 150 <= measure <= 193
        elif uom == 'in':
            return 59 <= measure <= 76
        return False
    except ValueError:  # This is needed to catch a single input with missing uom
        return False


def validator_hcl(value):
    return value[0] == '#' and len(value[1:]) == 6 and set(value[1:]).issubset(string.hexdigits)


def validator_ecl(value):
    return value in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


def validator_pid(value):
    return len(value) == 9


validators = {
    'byr': validator_byr,
    'iyr': validator_iyr,
    'eyr': validator_eyr,
    'hgt': validator_hgt,
    'hcl': validator_hcl,
    'ecl': validator_ecl,
    'pid': validator_pid,
}


def main(filename):
    with open(filename) as f:
        res = f.read().split('\n\n')
        valid_passports = 0
        for line in res:
            splitted_line = re.findall('[a-z]{3}:[a-z0-9#]{0,}', line)
            data = dict(x.split(":") for x in splitted_line)
            if all(key in data.keys() for key in validators.keys()):
                if all(validators[k](v) for k, v in data.items() if k != 'cid'):
                    valid_passports += 1
        return valid_passports


if __name__ == '__main__':
    print(main('input.txt'))
