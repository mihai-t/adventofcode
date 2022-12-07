import os

h, d = 0, 0


def forward(x):
    global h
    h += x


def down(x):
    global d
    d += x


def up(x):
    global d
    d -= x


if __name__ == '__main__':
    with open(os.path.join('inputs', 'day2.txt')) as f:
        moves = list(map(lambda x: x.split(' '), f.readlines()))
        moves = list(map(lambda x: (x[0], int(x[1])), moves))

    for q in moves:
        locals()[q[0]](q[1])
    print(h, d, h * d)
