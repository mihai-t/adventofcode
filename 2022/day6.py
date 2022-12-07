import os


def is_unique(token):
    return len(set(token)) == len(token)


def first_marker(token, ln):
    t = ""
    for i, c in enumerate(token):
        if len(t) == ln:
            t = t[1:]
        t += c
        if len(t) == ln and is_unique(t):
            return i + 1


if __name__ == '__main__':
    with open(os.path.join('inputs', 'day6.txt'), 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda x: x.strip(), lines))
        ln = lines[0]

    print(first_marker(ln, 14))
