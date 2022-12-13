import itertools
import os
from functools import cmp_to_key


def is_in_right_order_r(left, right, c=[]):
    if left is None and right is not None:
        # right order
        c.append(1)
    elif left is not None and right is None:
        # not right order
        c.append(-1)
    elif type(left) is int and type(right) is int:
        if left < right:
            # right order
            c.append(1)
        elif left == right:
            # should continue
            c.append(0)
        else:
            # not right order
            c.append(-1)
    elif type(left) is list and type(right) is list:
        for x, y in itertools.zip_longest(left, right):
            is_in_right_order_r(x, y, c)

    elif type(left) is int and type(right) is list:
        is_in_right_order_r([left], right, c)
    elif type(left) is list and type(right) is int:
        is_in_right_order_r(left, [right], c)
    else:
        raise ValueError(f"Got {left}, {right}")


def is_in_right_order(left, right):
    c = []
    is_in_right_order_r(left, right, c)
    for i in c:
        if i == 1:
            return 1
        elif i == -1:
            return -1
    return 1


if __name__ == '__main__':
    with open(os.path.join('inputs', 'day13.txt'), 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda x: x.strip(), lines))
        lines = list(filter(lambda x: x, lines))
        lines = list(map(lambda x: eval(x), lines))

    s = 0
    for pair, i in enumerate(range(0, len(lines) - 1, 2)):
        left = lines[i]
        right = lines[i + 1]
        if is_in_right_order(left, right) is 1:
            s += pair + 1
    print(s)

    div1, div2 = [[2]], [[6]]
    lines.append(div1)
    lines.append(div2)
    lines = sorted(lines, key=cmp_to_key(is_in_right_order), reverse=True)

    p = 1
    for i, ln in enumerate(lines):
        if ln in (div1, div2):
            p *= (i + 1)
    print(p)
