import os
from copy import deepcopy


class Rope:

    def __init__(self, head=(0, 0), tail=(0, 0)):
        self.head = list(head)
        self.tail = list(tail)
        self.visited_tail = {tail}

    def simple_move(self, x, y, dir) -> list:
        if dir == "R":
            return [x, y + 1]
        elif dir == "U":
            return [x - 1, y]
        elif dir == "L":
            return [x, y - 1]
        elif dir == "D":
            return [x + 1, y]
        else:
            raise ValueError(dir)

    def move(self, dir, c):
        for _ in range(c):
            old_head = deepcopy(self.head)
            self.head = self.simple_move(self.head[0], self.head[1], dir)
            if not self.are_touching():
                self.tail = old_head
                self.visited_tail.add(tuple(self.tail))

    def points_are_touching(self, x1, y1, x2, y2):
        return (x1 == x2 and y1 == y2) or (abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1)

    def are_touching(self):
        return self.points_are_touching(self.tail[0], self.tail[1], self.head[0], self.head[1])


class ExtendedRope(Rope):

    def __init__(self, tail_length=9):
        self.tail_length = tail_length
        self.positions = [[4, 0] for _ in range(tail_length + 1)]
        self.visited_tail = {tuple(self.positions[0])}

    def closest_point(self, p1, p2):
        m, best = 100, None
        for mm_x, mm_y in ((1, 1), (1, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (0, 1), (0, -1)):
            candidate = [p1[0] + mm_x, p1[1] + mm_y]
            dist = abs(candidate[0] - p2[0]) + abs(candidate[1] - p2[1])
            if dist < m:
                m, best = dist, candidate

        return best

    def move(self, dir, c):
        for _ in range(c):
            self.positions[-1] = self.simple_move(self.positions[-1][0], self.positions[-1][1], dir)
            pos = len(self.positions) - 2
            while self.are_touching() is not False and pos >= 0:
                my_pos = self.positions[pos]
                next_pos = self.positions[pos + 1]
                self.positions[pos] = self.closest_point(my_pos, next_pos)
                pos -= 1

            self.visited_tail.add(tuple(self.positions[0]))

    def are_touching(self):
        for i in range(0, len(self.positions) - 1):
            if not self.points_are_touching(self.positions[i][0], self.positions[i][1], self.positions[i + 1][0],
                                            self.positions[i + 1][1]):
                return i
        return False

    def print_state(self):
        for i in range(0, 5):
            for j in range(0, 6):
                found = False
                for ind, (x1, y1) in enumerate(reversed(self.positions)):
                    if x1 == i and y1 == j:
                        if ind == 0:
                            print("H", end="")
                        elif ind == len(self.positions) - 1:
                            print("T", end="")
                        else:
                            print(ind, end="")
                        found = True
                        break
                if not found:
                    print(".", end="")
            print()
        print("=" * 50)


if __name__ == '__main__':
    with open(os.path.join('inputs', 'day9.txt'), 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda x: x.strip(), lines))

    r = Rope()
    for l in lines:
        dir = l.split(" ")[0]
        c = int(l.split(" ")[1])
        r.move(dir, c)
    print(f"Tail visited {len(r.visited_tail)} positions")

    r = ExtendedRope()
    for l in lines:
        dir = l.split(" ")[0]
        c = int(l.split(" ")[1])
        r.move(dir, c)
    print(f"Tail visited {len(r.visited_tail)} positions")
