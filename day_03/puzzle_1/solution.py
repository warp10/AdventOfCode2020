#!/usr/bin/env python3


def load_map(file):
    array = []
    for line in file.readlines():
        line = line.strip()
        sub_array = []
        for item in line:
            sub_array.append(True if item == '#' else False)
        array.append(sub_array)
    return array


def main(filename):
    with open(filename) as f:
        map = load_map(f)
        length = len(map[0])
        pos = 4
        trees = 0
        for line in map[1:]:
            if line[pos-1]:
                trees += 1
            pos = (pos + 3) % length
        return trees


if __name__ == '__main__':
    print(main('input.txt'))
