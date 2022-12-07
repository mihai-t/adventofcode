import os
from functools import reduce


def bf(lines, point):
    x, y = point
    q = [(x, y)]
    visited = set()
    while q:
        item = q.pop(0)
        visited.add(item)
        i, j = item[0], item[1]
        for ii, jj in [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]:
            if ii < 0 or ii >= len(lines) or jj < 0 or jj >= len(lines[i]):
                continue
            if (ii, jj) in visited:
                continue
            if lines[ii][jj] == '9':
                continue
            q.append((ii, jj))
    return len(visited)


if __name__ == '__main__':
    with open(os.path.join('inputs', 'day9.txt'), 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
    l = []
    lowest_points = []
    for i in range(len(lines)):
        for j in range(0, len(lines[i])):
            item = lines[i][j]
            lowest = True
            for ii, jj in [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]:
                if ii < 0 or ii >= len(lines) or jj < 0 or jj >= len(lines[i]):
                    continue
                if item >= lines[ii][jj]:
                    lowest = False
            if lowest:
                l.append(int(item) + 1)
                lowest_points.append((i, j))
    print(sum(l))

    sizes = []
    for point in lowest_points:
        sizes.append(bf(lines, point))
    print(reduce(lambda x, y: x * y, sorted(sizes)[-3:]))
