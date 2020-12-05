#!/usr/bin/env python3


def main(filename):
    valid_passwords = 0
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip().split(' ')
            min, max = line[0].split('-')
            letter = line[1][:-1]
            password = line[2]
            if int(min) <= password.count(letter) <= int(max):
                valid_passwords += 1

    return valid_passwords


if __name__ == '__main__':
    print(main('input.txt'))
