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


def find_missing_seat(seats):
    missing_seats = []
    # Just a brute-force approach, I wasn't interested in finding an elegant
    # solution
    for position, seat in enumerate(seats):
        try:
            if seats[position + 1] != seat + 1:
                missing_seats.append(seat + 1)
        except IndexError:
            # This just means we reached the end of the list
            pass
    return missing_seats


def main(filename):
    seats = []
    with open(filename) as f:
        for line in f.readlines():
            row, column = get_seat_data(line.strip())
            seat_id = get_seat_id(row, column)
            seats.append(seat_id)
    return find_missing_seat(sorted(seats))


if __name__ == '__main__':
    print(main('input.txt'))
