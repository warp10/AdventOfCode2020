#!/usr/bin/env python3


def main(filename):
    with open(filename) as f:
        groups = f.read().split('\n\n')
        counter = 0
        for group in groups:
            counter += len(set(group.replace('\n', '')))
        return counter


if __name__ == '__main__':
    print(main('input.txt'))


