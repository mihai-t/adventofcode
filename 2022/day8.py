import os

import numpy as np


def is_visible(x, y, mat):
    if max(mat[x, y + 1:]) < mat[x][y]:
        return True
    if max(mat[x, :y]) < mat[x][y]:
        return True
    if max(mat[x + 1:, y]) < mat[x][y]:
        return True
    if max(mat[:x, y]) < mat[x][y]:
        return True
    return False


def score(x, y, mat):
    s = 1
    e = mat[x][y]
    for m, d in zip((mat[x, y + 1:], mat[x + 1:, y], mat[:x, y], mat[x, :y]), (0, 0, -1, -1)):
        ind = np.where(m - e >= 0)[0]
        if len(ind) > 0:
            if d == 0:
                sc = ind[d] + 1
            else:
                sc = len(m) - ind[-1]
        else:
            sc = len(m)
        s *= sc
    return s


if __name__ == '__main__':
    with open(os.path.join('inputs', 'day8.txt'), 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda x: x.strip(), lines))
        mat = list(map(lambda x: [int(q) for q in x], lines))
        mat = np.array(mat)
    visible = 2 * len(mat[0]) + 2 * (len(mat) - 2)

    best = 0
    for i in range(1, len(mat) - 1):
        for j in range(1, len(mat[0]) - 1):
            if is_visible(i, j, mat):
                visible += 1
            sc = score(i, j, mat)
            if sc > best:
                best = sc

    print(visible)
    print(best)
