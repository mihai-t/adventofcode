import os


def step(lines):
    flashes = list()
    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
            e = int(lines[i][j])
            e += 1
            if e > 9:
                flashes.append((i, j))
                lines[i][j] = 0
            else:
                lines[i][j] = e

    n = 0
    while n < len(flashes):
        i, j = flashes[n]
        for ii, jj in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j), (i, j + 1), (i + 1, j - 1),
                       (i + 1, j), (i + 1, j + 1)]:
            if ii < 0 or ii >= len(lines) or jj < 0 or jj >= len(lines[ii]):
                continue
            if (ii, jj) in flashes:
                continue
            e = int(lines[ii][jj])
            e += 1
            if e > 9:
                flashes.append((ii, jj))
                lines[ii][jj] = 0
            else:
                lines[ii][jj] = e

        n += 1

    return lines, len(flashes), sum([sum(l) for l in lines]) == 0


if __name__ == '__main__':
    with open(os.path.join('inputs', 'day11.txt'), 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda x: x.strip(), lines))
        lines = [[int(x) for x in lines[i]] for i in range(0, len(lines))]
    total = 0
    for q in range(500):
        lines, flashes, all_flash = step(lines)
        total += flashes
        if all_flash:
            print(q + 1, 'step', total, 'flashes', 'ALL FLASH!')
        else:
            print(q + 1, 'step', total, 'flashes')
