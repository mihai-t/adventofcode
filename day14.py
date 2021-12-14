import os
from copy import copy


def transform(initial, rules):
    res = initial[0]
    for i in range(0, len(initial) - 1):
        ss = initial[i:i + 2]
        if ss in rules:
            res += rules[ss] + ss[1]
        else:
            assert False
            # res += ss[1]
    return res


def count_chr(initial):
    count = {}
    for a in initial:
        count[a] = count.get(a, 0) + 1
    return count


def transform_count_pairs(count_pairs, rules):
    count_new = {}
    for k, v in count_pairs.items():
        new_pair_1 = k[0] + rules[k]
        new_pair_2 = rules[k] + k[1]
        count_new[new_pair_1] = count_new.get(new_pair_1, 0) + v
        count_new[new_pair_2] = count_new.get(new_pair_2, 0) + v
    return count_new


def count_in_pairs(count_pairs, last_elem):
    count = {last_elem: 1}
    for k, v in count_pairs.items():
        count[k[0]] = count.get(k[0], 0) + v
        # count[k[1]] = count.get(k[1], 0) + v
    return count


if __name__ == '__main__':
    with open(os.path.join('inputs', 'day14.txt'), 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda x: x.strip(), lines))
        lines = list(filter(lambda x: x, lines))
        initial = lines[0]
        rules = list(map(lambda x: x.split('->'), lines[1:]))
        rules = {k.strip(): v.strip() for k, v in rules}
    print(initial)
    print(rules)

    conf = copy(initial)
    for i in range(10):
        conf = transform(conf, rules)
        c = count_chr(conf)
        maxx = max(c.values())
        minn = min(c.values())
        print(i + 1, maxx - minn)
    print('-----')
    cnt_pairs = {}
    for i in range(len(initial) - 1):
        p = initial[i] + initial[i + 1]
        cnt_pairs[p] = cnt_pairs.get(p, 0) + 1

    for i in range(40):
        cnt_pairs = transform_count_pairs(cnt_pairs, rules)
        c = count_in_pairs(cnt_pairs, initial[-1])

        maxx = max(c.values())
        minn = min(c.values())
        print(i + 1, maxx - minn)
