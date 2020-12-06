#!/usr/bin/env python3


def main(filename):
    with open(filename) as f:
        groups = f.read().split('\n\n')
        counter = 0
        for group in groups:
            answers = [set(answer) for answer in group.strip().split('\n')]
            counter += len(set.intersection(*answers))
        return counter


if __name__ == '__main__':
    print(main('input.txt'))


