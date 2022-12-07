import os


def pr(common):
    if common.lower() == common:
        priority = ord(common) - ord('a') + 1
    else:
        priority = ord(common) - ord('A') + 27
    return priority


if __name__ == '__main__':

    s = 0
    s2 = 0
    with open(os.path.join('inputs', 'day3.txt'), 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda x: x.strip(), lines))

    for ln in lines:
        ln = ln.strip()
        fs, sn = ln[:len(ln) // 2], ln[len(ln) // 2:]
        common = [x for x in fs if x in sn][0]

        s += pr(common)

    for i in range(0, len(lines) - 2, 3):
        f1, f2, f3 = lines[i], lines[i + 1], lines[i + 2]

        common = [x for x in f1 if x in f2 and x in f3][0]
        s2 += pr(common)

    print(s)
    print(s2)
