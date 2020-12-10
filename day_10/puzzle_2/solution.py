#!/usr/bin/env python3

import collections


def main(filename):
    with open(filename) as f:
        joltages_list = [int(joltage) for joltage in f.readlines()]
        joltages_list += [max(joltages_list) + 3]
        joltages_list.sort()

        counts = collections.Counter({0: 1})
        for joltage in joltages_list:
            counts[joltage] = counts[joltage - 1] + counts[joltage - 2] + counts[joltage - 3]

        return counts[joltage]


if __name__ == '__main__':
    print(main('input.txt'))
