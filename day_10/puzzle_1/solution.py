#!/usr/bin/env python3


def couple_joltages(joltages_list):
    i = 0
    j = 2
    coupled_joltages = []
    while j <= len(joltages_list):
        coupled_joltages.append(joltages_list[i:j])
        i += 1
        j += 1
    return coupled_joltages


def main(filename):
    with open(filename) as f:
        joltages_list = [int(joltage) for joltage in f.readlines()]
        joltages_list += [0, max(joltages_list) + 3]
        joltages_list.sort()

        differences = [b - a for a, b in couple_joltages(joltages_list)]
        return differences.count(1) * differences.count(3)


if __name__ == '__main__':
    print(main('input.txt'))
