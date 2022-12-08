class Die:

    def __init__(self, times=3, maxx=100):
        self.c = 1
        self.maxx = maxx
        self.times = times
        self.counts = 0

    def roll(self):
        rolls = []
        for _ in range(self.times):

            rolls.append(self.c)
            self.c += 1
            if self.c > self.maxx:
                self.c = 1
            self.counts += 1
        return rolls


class Player:

    def __init__(self, pos, maxx=10):
        self.pos = pos
        self.maxx = maxx
        self.score = 0

    def move(self, steps):
        self.pos = self.pos + steps
        r = self.pos % self.maxx
        if r == 0:
            self.pos = self.maxx
        else:
            self.pos = r

        self.score += self.pos


if __name__ == '__main__':

    die = Die(times=3, maxx=100)
    p1, p2 = Player(4, maxx=10), Player(8, maxx=10)
    # p1, p2 = Player(8, maxx=10), Player(6, maxx=10)
    MAXX = 1000
    while p1.score < MAXX and p2.score < MAXX:
        steps = die.roll()
        moves = sum(steps)
        p1.move(moves)
        # print(f"Player 1 rolls {steps} and moves to space {p1.pos} for a total score of {p1.score}")
        if p1.score >= MAXX:
            break
        steps = die.roll()
        moves = sum(steps)
        p2.move(moves)

        # print(f"Player 2 rolls {steps} and moves to space {p2.pos} for a total score of {p2.score}")

    if p1.score > p2.score:
        print(p2.score * die.counts)
    else:
        print(p1.score * die.counts)
