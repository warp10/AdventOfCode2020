#!/usr/bin/env python3

data = {}


def load_lines(lines):
    """
    Structure of data:
    {key_color: [(color1, qty1), (color2, qty2), ...]}
    """
    global data
    for line in lines:
        key, content = line.split(' bags contain ')
        if content == 'no other bags.':
            data[key] = [('no bags', 0)]
        else:
            values = []
            raw_values = content.split(', ')
            for raw_value in raw_values:
                qty, raw_color = raw_value.split(' ', 1)
                color, _ = raw_color.rsplit(' ', 1)
                values.append((color, int(qty)))
            data[key] = values


def count_bags(values):
    """
    Structure of values:
    [(color1, qty1), (color2, qty2), ...]
    """
    if values[0][0] == 'no bags':
        return 0

    return sum(v[1] + v[1] * count_bags(data[v[0]]) for v in values)


def main(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        load_lines(lines)

    return count_bags(data['shiny gold'])


if __name__ == '__main__':
    print(main('input.txt'))
