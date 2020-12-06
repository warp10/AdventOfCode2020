#!/usr/bin/env python3


def get_number(string, char):
    valid = int(string[0] == char)
    if len(string) == 1:
        return valid
    else:
        exp = (len(string) - 1) * valid
        return valid * 2 ** exp + get_number(string[1:], char)


def get_seat_data(string):
    row = get_number(string[:7], 'B')
    column = get_number(string[7:], 'R')
    return row, column


def get_seat_id(row, column):
    return row * 8 + column


def main(filename):
    with open(filename) as f:
        seat_id = 0
        for line in f.readlines():
            row, column = get_seat_data(line.strip())
            new_seat_id = get_seat_id(row, column)
            # I know this could be done with a proper max(), but it looks way
            # more readable this way
            if new_seat_id > seat_id:
                seat_id = new_seat_id
    return seat_id


if __name__ == '__main__':
    print(main('input.txt'))


"""
LLL = 0+0+0 = 0
LLR = 0+0+1 = 1
LRL = 0+2+0 = 2
LRR = 0+2+1 = 3
RLL = 4+0+0 = 4
RLR = 4+0+1 = 5
RRL = 4+2+0 = 6
RRR = 4+2+1 = 7
"""
