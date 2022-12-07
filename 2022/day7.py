import os

CURRENT = None
DIRS = {}
TOTAL = 70000000
MIN_TO_FREE = 30000000


def add_size(DIRS, current_path, f_name, size):
    for d in list(DIRS.keys()):
        if d in current_path:
            DIRS[d] += size


if __name__ == '__main__':
    with open(os.path.join('inputs', 'day7.txt'), 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda x: x.strip(), lines))

    is_ls = False
    for ln in lines:
        if ln.startswith("$ cd"):
            is_ls = False
            cd_to = ln[5:]
            if cd_to == "/":
                CURRENT = "/"
            elif cd_to == "..":
                CURRENT = os.path.dirname(CURRENT)
            else:
                CURRENT = os.path.join(CURRENT, cd_to)
            if CURRENT not in DIRS:
                DIRS[CURRENT] = 0
        elif ln.startswith("$ ls"):
            is_ls = True
        elif is_ls:
            tokens = ln.split(' ')
            if tokens[0] == "dir":
                if os.path.join(CURRENT, tokens[1]) not in DIRS:
                    DIRS[os.path.join(CURRENT, tokens[1])] = 0
            else:
                add_size(DIRS, CURRENT, tokens[1], int(tokens[0]))

    s = 0
    for k, v in DIRS.items():
        if v <= 100000:
            s += v
    print(s)

    free_space = TOTAL - DIRS["/"]
    needed = MIN_TO_FREE - free_space
    mn = DIRS["/"]
    for k, v in DIRS.items():
        if needed <= v < mn:
            mn = v
    print(mn)
