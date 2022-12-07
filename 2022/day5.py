import os
from copy import deepcopy


def move(stacks, count, frm, to, reverse=True):
    to_move = stacks[frm][:count]
    if reverse:
        to_move = to_move[::-1]
    stacks[frm] = stacks[frm][count:]
    stacks[to] = to_move + stacks[to]
    return stacks


if __name__ == '__main__':
    with open(os.path.join('inputs', 'day5.txt'), 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda x: x.replace('\n', ''), lines))

    ovr = 0
    ovr2 = 0
    moves = False

    stacks = []
    stacks2 = None
    for ln in lines:

        if '1' in ln and not moves:
            continue
        if not ln:
            moves = True
            stacks2 = deepcopy(stacks)
            continue
        if moves:
            tokens = ln.split(" ")
            stacks = move(stacks, int(tokens[1]), int(tokens[3]) - 1, int(tokens[5]) - 1)
            stacks2 = move(stacks2, int(tokens[1]), int(tokens[3]) - 1, int(tokens[5]) - 1, reverse=False)

        else:
            for c in range(5, 3, -1):
                t = " " * c
                ln = ln.replace(t, "~N~")
            ln = ln.replace(" ", "")

            for i, q in enumerate(range(0, len(ln), 3)):
                token = ln[q:q + 3]

                if len(stacks) <= i:
                    stacks.append("")
                if token != "~N~":
                    stacks[i] += token.replace('[', '').replace(']', '')

    for s in stacks:
        if s:
            print(s[0], end='')
    print()

    for s in stacks2:
        if s:
            print(s[0], end='')
    print()

