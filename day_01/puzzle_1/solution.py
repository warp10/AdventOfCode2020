#!/usr/bin/env python3


def main_unoptimized(filename):
    # This is the first, unoptimized, O(n^2) version
    with open(filename) as f:
        res = [int(item.strip()) for item in f.readlines()]
        for item1 in res:
            for item2 in res:
                if item1 + item2 == 2020:
                    return item1*item2


def main(filename):
    with open(filename) as f:
        res = [int(item.strip()) for item in f.readlines()]
        res.sort()
        start = 0
        end = -1
        while True:
            if res[start] + res[end] == 2020:
                return res[start] * res[end]
            elif res[start] + res[end] < 2020:
                start += 1
            elif res[start] + res[end] > 2020:
                end -= 1


if __name__ == '__main__':
    print(main('input.txt'))
