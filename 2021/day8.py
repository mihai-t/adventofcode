import os


def is_1(token):
    return len(set(token)) == 2


def is_4(token):
    return len(set(token)) == 4


def is_7(token):
    return len(set(token)) == 3


def is_8(token):
    return len(set(token)) == 7


def is_0_or_6_or_9(token):
    return len(set(token)) == 6


def count_1_4_7_8(tokens):
    c = 0
    for t in tokens:
        if is_1(t) or is_4(t) or is_7(t) or is_8(t):
            c += 1
    return c


def decode_digit(right, digit_map):
    n = ''
    inv_d_m = {v: k for k, v in digit_map.items()}
    for t in right:
        if is_1(t):
            n += '1'
        elif is_4(t):
            n += '4'
        elif is_7(t):
            n += '7'
        elif is_8(t):
            n += '8'
        elif is_0_or_6_or_9(t):
            not_6, not_0, not_9 = False, False, False
            for d in t:
                if digit_map[d] == 3:
                    not_6 = True
                elif digit_map[d] == 7:
                    not_0 = True
                elif digit_map[d] == 6:
                    not_9 = True
            if not_9 and not_6:
                n += '0'
            elif not_0 and not_9:
                n += '6'
            elif not_0 and not_6:
                n += '9'
            else:
                assert False
        else:  # 5, 2,3
            if inv_d_m[1] not in t and inv_d_m[6] not in t:
                n += '3'
            elif inv_d_m[6] not in t and inv_d_m[3] not in t:
                n += '5'
            elif inv_d_m[1] not in t and inv_d_m[4] not in t:
                n += '2'
            else:
                assert False

    return int(n)


def decode(left, right):
    digit_map = {}
    four, one, seven, eight = None, None, None, None
    zero_six_nine = []
    for t in left:
        if is_1(t):
            one = t
        elif is_4(t):
            four = t
        elif is_7(t):
            seven = t
        elif is_0_or_6_or_9(t):
            zero_six_nine.append(t)
        elif is_8(t):
            eight = t
        else:
            continue

    opposite_four = {next(iter(set(zero_six_nine[0]) - set(zero_six_nine[1]))),
                     next(iter(set(zero_six_nine[1]) - set(zero_six_nine[0]))),
                     next(iter(set(zero_six_nine[1]) - set(zero_six_nine[2])))}
    assert len(opposite_four) == 3
    for c in opposite_four:
        if c in one:
            digit_map[c] = 3
    for c in one:
        if c not in digit_map:
            digit_map[c] = 4
    for c in seven:
        if c not in digit_map:
            digit_map[c] = 2
    for c in opposite_four:
        if c in four and c not in digit_map:
            digit_map[c] = 7
    for c in four:
        if c not in digit_map:
            digit_map[c] = 1
    for c in opposite_four:
        if c not in digit_map:
            digit_map[c] = 6
    for c in eight:
        if c not in digit_map:
            digit_map[c] = 5
    assert len(digit_map) == 7
    return decode_digit(right, digit_map)


if __name__ == '__main__':
    with open(os.path.join('inputs', 'day8.txt'), 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda x: x.split('|'), lines))
        left, right = list(map(lambda x: x[0].strip().split(' '), lines)), list(
            map(lambda x: x[1].strip().split(' '), lines))

    print(sum([count_1_4_7_8(t) for t in right]))

    print(sum([decode(l, r) for l, r in zip(left, right)]))
