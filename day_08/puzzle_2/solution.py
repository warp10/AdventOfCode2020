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
        self.program = program  # Raw program as read from filw
        self.code = []  # Each line of program is converted into a tuple (ops, arg)
        self.patch_pointer = 0  # This is a pointer to the last patched op
        self.load_program()

    def load_program(self):
        for line in self.program:
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

    def reset_and_patch_program(self):
        """
        Reset all registries (except for patch_counter), reloads and patch the program
        """
        self.accumulator = 0
        self.ip = 0
        self.recorded_ips = []
        self.code = []
        self.load_program()
        self.patch_code()

    def patch_code(self):
        # This is really ugly :()
        for line in self.code[self.patch_pointer:]:
            if line[0] in ('nop, jmp'):
                pos = self.code.index(line, self.patch_pointer)
                self.patch_pointer = pos + 1
                newop = 'jmp' if self.code[pos][0] == 'nop' else 'nop'
                self.code[pos] = (newop, self.code[pos][1])
                return

    def run_program(self):
        self.patch_code()
        while self.ip < len(self.code):
            op, arg = self.code[self.ip]
            self.record_ip()
            self.ops[op](arg)
            if self.is_infinite_loop():
                self.reset_and_patch_program()

        return self.accumulator


def main(filename):
    with open(filename) as f:
        gb = GameBoy(f.readlines())
    return gb.run_program()


if __name__ == '__main__':
    print(main('input.txt'))
