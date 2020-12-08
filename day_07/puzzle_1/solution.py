#!/usr/bin/env python3

data = {}


def load_lines(lines):
    """Structure of data:
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
                values.append((color, qty))
            data[key] = values


def is_valid_bag(values):
    # memoization would have been nice here, but it was not worth writing it
    # given the small input
    colors = [value[0] for value in values]
    if 'shiny gold' in colors:
        return True
    elif 'no bags' in colors:
        return False

    return any(is_valid_bag(data[color]) for color in colors)


def main(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        load_lines(lines)

    return sum(is_valid_bag(values) for values in data.values())


if __name__ == '__main__':
    print(main('input.txt'))
