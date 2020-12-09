#!/usr/bin/env python3


from itertools import permutations


def main(filename, preamble_length):
    with open(filename) as f:
        numbers = [int(number.strip()) for number in f.readlines()]
        preamble_end = preamble_length
        for number in numbers[preamble_end:]:
            preamble = numbers[preamble_end-preamble_length:preamble_end]
            if number not in [sum(item) for item in permutations(preamble, 2)]:
                return number
            preamble_end += 1


if __name__ == '__main__':
    print(main('input.txt', preamble_length=25))
