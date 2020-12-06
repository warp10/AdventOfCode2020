#!/usr/bin/env python3


def main(filename):
    with open(filename) as f:
        res = [int(item.strip()) for item in f.readlines()]
        # I know this is O(n^3), yet the data is reasonably short and quick
        # to process, so I don't care about optimizing this algorithm
        for item1 in res:
            for item2 in res:
                for item3 in res:
                    if item1 + item2 + item3 == 2020:
                        return item1 * item2 * item3


if __name__ == '__main__':
    print(main('input.txt'))
