import os
from copy import deepcopy
from math import inf


def top_down(lines):
    def is_n(ii, jj, ii2, jj2):
        return 0 < abs(ii - ii2) + abs(jj - jj2) < 2

    x, y = len(lines) - 1, len(lines[-1]) - 1
    n, m = x + 1, y + 1
    risk_mat = deepcopy(lines)
    q = [(x, y)]
    v = set()
    while q:
        x, y = q.pop(0)
        if (x, y) in v:
            continue
        v.add((x, y))

        mn = inf
        for item in v:
            ii, jj = item
            if is_n(ii, jj, x, y) and risk_mat[ii][jj] < mn:
                mn = risk_mat[ii][jj]
        if mn != inf:
            risk_mat[x][y] = lines[x][y] + mn
            if x == 0 and y == 0:
                break
        for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if i < 0 or j < 0 or i >= n or j >= m:
                continue
            if (i, j) in v:  # visited
                continue
            q.append((i, j))

    return risk_mat


def minCost(cost, row, col):
    # https://www.geeksforgeeks.org/min-cost-path-dp-6/ O(n^2)
    # For 1st column
    for i in range(1, row):
        cost[i][0] += cost[i - 1][0]

    # For 1st row
    for j in range(1, col):
        cost[0][j] += cost[0][j - 1]

    # For rest of the 2d matrix
    for i in range(1, row):
        for j in range(1, col):
            cost[i][j] += (min(cost[i - 1][j], cost[i][j - 1]))

    # Returning the value in
    # last cell
    return cost[row - 1][col - 1]


# Driver program to test above functions
def increase_matr(lines, c=1):
    lines = deepcopy(lines)
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            lines[i][j] += c
            if lines[i][j] > 9:
                lines[i][j] = 1
    return lines


def build_big_matr(lines):
    final = deepcopy(lines)

    for j in range(1, 5):
        lines = increase_matr(lines, 1)
        for q in range(0, len(final)):
            final[q] += lines[q]

    lines = deepcopy(final)
    for i in range(1, 5):
        lines = increase_matr(lines, 1)
        for l in lines:
            final.append(l)

    return final


if __name__ == '__main__':
    with open(os.path.join('inputs', 'day15.txt'), 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda x: x.strip(), lines))
        lines = [[int(a) for a in l] for l in lines]

    print(minCost(deepcopy(lines), len(lines), len(lines[-1])) - lines[0][0])
    big_matr = build_big_matr(lines)
    print(minCost(big_matr, len(big_matr), len(big_matr[-1])) - big_matr[0][0])

