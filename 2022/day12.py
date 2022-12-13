import os

import numpy as np


def can_step(from_l, to_l):
    if from_l == "S":
        if to_l in ("a", "b"):
            return True
        return False
    if to_l == "E":
        if from_l in ('y', 'z'):
            return True
        else:
            return False
    return ord(to_l) - ord(from_l) <= 1


def bf(mz, s_x, s_y, not_larger_than=None):
    q = [(s_x, s_y)]
    distances = np.zeros(shape=mz.shape, dtype=np.uint32)
    n, m = len(mz), len(mz[0])
    while q:
        x, y = q[0]
        del q[0]
        for (i, j) in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            x1, y1 = x + i, y + j
            if 0 <= x1 < n and 0 <= y1 < m and (x1 != s_x or y1 != s_y):
                if distances[x1, y1] == 0 and can_step(mz[x, y], mz[x1, y1]):
                    distances[x1, y1] = distances[x, y] + 1
                    # print(f"Distance to {x1}:{y1} through {x}:{y} is {distances[x1, y1]}")
                    q.append((x1, y1))
                    if mz[x1, y1] == "E":
                        if not_larger_than is None:
                            return int(distances[x1, y1])
                        return int(min(not_larger_than, distances[x1, y1]))
    return min_distance


if __name__ == '__main__':
    with open(os.path.join('inputs', 'day12.txt'), 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda x: x.strip(), lines))
        mz = [[x for x in line] for line in lines]
    mz = np.array(mz)
    a_positions = []
    for i in range(0, len(mz)):
        for j in range(0, len(mz[i])):
            if mz[i, j] == "S":
                x, y = i, j
            if mz[i, j] == "E":
                x1, y1 = i, j
            if mz[i, j] == "a":
                a_positions.append((i, j))

    min_distance = bf(mz, x, y, not_larger_than=None)
    print(f"From {x}:{y} to {x1}:{y1} in {min_distance} steps")

    print(f"Analysing {len(a_positions)}")
    for i, (x, y) in enumerate(a_positions):
        new_min_distance = bf(mz, x, y, not_larger_than=min_distance)
        if new_min_distance < min_distance:
            min_distance = new_min_distance
            print(f"{i}. From {x}:{y} to {x1}:{y1} in {min_distance} steps")
