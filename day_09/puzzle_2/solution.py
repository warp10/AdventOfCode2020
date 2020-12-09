#!/usr/bin/env python3


def main(filename, number):
    with open(filename) as f:
        numbers = [int(number.strip()) for number in f.readlines()]
        for pos in range(len(numbers)):
            numbers_list = []
            for num in numbers[pos:]:
                numbers_list.append(num)
                if sum(numbers_list) == number:
                    return min(numbers_list) + max(numbers_list)
                elif sum(numbers_list) > number:
                    break


if __name__ == '__main__':
    print(main('input.txt', number=138879426))
