#!/usr/bin/env python3


def load_map(file):
    array = []
    for line in file.readlines():
        line = line.strip()
        sub_array = []
        for item in line:
            # Converting '#' to True to make checks easier in main()
            sub_array.append(True if item == '#' else False)
        array.append(sub_array)
    return array


def main(filename, starting_position=4, rows_to_skip=0):
    # This is the least maintainable code ever.
    with open(filename) as f:
        map = load_map(f)
        length = len(map[0])
        pos = starting_position
        trees = 0
        for line_number, line in enumerate(map[1:], 1):
            if line_number % (rows_to_skip + 1):
                continue
            if line[pos - 1]:
                trees += 1
            pos = (pos + starting_position - 1) % length
        return trees


if __name__ == '__main__':
    print(
        main('input.txt', 2, 0) *
        main('input.txt', 4, 0) *
        main('input.txt', 6, 0) *
        main('input.txt', 8, 0) *
        main('input.txt', 2, 1)
    )
