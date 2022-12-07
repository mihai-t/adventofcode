import os

h, d, aim = 0, 0, 0


def forward(x):
    global h, d, aim
    h += x
    d += aim * x


def down(x):
    global aim
    aim += x


def up(x):
    global aim
    aim -= x


if __name__ == '__main__':
    with open(os.path.join('inputs', 'day2.txt')) as f:
        moves = list(map(lambda x: x.split(' '), f.readlines()))
        moves = list(map(lambda x: (x[0], int(x[1])), moves))

    for q in moves:
        locals()[q[0]](q[1])
    print(h, d, h * d)
