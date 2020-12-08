#!/usr/bin/env python3


class GameBoy():
    def __init__(self, program):
        self.accumulator = 0
        self.ip = 0  # Instruction_pointer
        self.recorded_ips = []  # Used by is_infinite_loop()
        self.ops = {
            'acc': self.acc,
            'jmp': self.jmp,
            'nop': self.nop
        }
        self.code = []  # Each line of program is converted into a tuple (ops, arg)
        self.load_program(program)

    def load_program(self, program):
        for line in program:
            op, arg = line.strip().split(' ')
            self.code.append((op, int(arg)))

    def acc(self, arg):
        self.accumulator += arg
        self.ip += 1

    def jmp(self, arg):
        self.ip += arg

    def nop(self, arg):
        self.ip += 1

    def record_ip(self):
        """
        This is used by the infinite loop detector.
        It must be executed before the op is
        """
        self.recorded_ips.append(self.ip)

    def is_infinite_loop(self):
        """
        This is the infinite loop detector.
        It must be run at the end of the main cycle
        """
        return self.ip in self.recorded_ips

    def run_program(self):
        while True:
            op, arg = self.code[self.ip]
            self.record_ip()
            self.ops[op](arg)
            if self.is_infinite_loop():
                return self.accumulator


def main(filename):
    with open(filename) as f:
        gb = GameBoy(f)
    return gb.run_program()


if __name__ == '__main__':
    print(main('input.txt'))
