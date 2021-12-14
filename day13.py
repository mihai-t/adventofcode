import os
from copy import copy


def do_fold(lines, fold):
    # y is horizontal
    new_lines = set()
    pos = fold[1]
    for line in lines:
        x, y = line
        if fold[0] == 'y':
            # change 2nd dim
            change = y - pos
            if change > 0:
                y = pos - change
        else:
            # change 1st dim
            change = x - pos
            if change > 0:
                x = pos - change
        new_lines.add((x, y))
    return new_lines


def print_mat(lines):
    # lines
    n = max(map(lambda x: x[1], lines))
    # columns
    m = max(map(lambda x: x[0], lines))

    mat = [['.' for _ in range(m + 1)] for _ in range(n + 1)]

    for l in lines:
        x, y = l[1], l[0]
        mat[x][y] = '#'
    for mt in mat:
        for mm in mt:
            print(mm, end='')
        print()


if __name__ == '__main__':
    with open(os.path.join('inputs', 'day13.txt'), 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda x: x.strip(), lines))
        lines = list(filter(lambda x: x, lines))
        fold = list(filter(lambda x: 'fold' in x, lines))
        lines = list(filter(lambda x: 'fold' not in x, lines))
        lines = set(map(lambda x: (int(x.split(',')[0]), int(x.split(',')[1])), lines))
        fold = list(map(lambda x: x.replace('fold along ', ''), fold))
        fold = list(map(lambda x: (x.split('=')[0], int(x.split('=')[1])), fold))

    lines_p1 = do_fold(copy(lines), fold[0])
    print(len(lines_p1))
    for f in fold:
        lines = do_fold(lines, f)
    print_mat(lines)
