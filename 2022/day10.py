import os


class CPU:

    def __init__(self, x=1):
        self.x = x
        self.s1 = 0
        self.cycle_ended = 0
        self.draw_array = []

    def sprite_position(self):
        return self.x, self.x + 1, self.x + 2

    def verify(self):
        assert self.x <= 40
        if self.cycle_ended in (20, 60, 100, 140, 180, 220):
            print(self.cycle_ended, self.x, self.cycle_ended * self.x)
            self.s1 += (self.cycle_ended * self.x)

    def draw(self):
        pos = self.cycle_ended + 1
        if pos // 40 == pos / 40:
            pos = 40
        else:
            pos = pos % 40
        sp = self.sprite_position()
        if pos in sp:
            self.draw_array.append("#")
        else:
            self.draw_array.append(".")

    def noop(self):
        self.draw()
        self.cycle_ended += 1
        self.verify()

    def addx(self, v):
        self.draw()
        self.cycle_ended += 1

        self.draw()
        self.verify()
        self.cycle_ended += 1

        self.verify()
        self.x += v

    def print(self):
        for k in range(0, 240, 40):
            print("".join(self.draw_array[k:k + 40]))


if __name__ == '__main__':
    with open(os.path.join('inputs', 'day10.txt'), 'r') as f:
        lines = f.readlines()
        instructions = list(map(lambda x: x.strip(), lines))

    cpu = CPU()
    for instr in instructions:
        if instr == "noop":
            cpu.noop()
        elif instr.startswith("addx"):
            v = int(instr.split(" ")[1])
            cpu.addx(v)
    print(cpu.s1)

    cpu.print()
