import os

cs = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

completion_score = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def check_closes(el_old, el_new):
    if el_old == '(' and el_new == ')':
        return True
    if el_old == '[' and el_new == ']':
        return True
    if el_old == '{' and el_new == '}':
        return True
    if el_old == '<' and el_new == '>':
        return True
    return False


def complete_line(st):
    score = 0
    completion_string = ''
    while st:
        el = st.pop()
        for e in completion_score.keys():
            if check_closes(el, e):
                score *= 5
                score += completion_score[e]
                completion_string += e
                break
    return score, completion_string


def get_score(line):
    st = []
    corupt_elem = None
    for l in line:
        is_close = l in cs.keys()
        if not is_close:
            st.append(l)
        else:
            if not st:
                corupt_elem = l
                break

            el = st.pop()
            if not check_closes(el, l):
                corupt_elem = l
                break
    if corupt_elem is None:
        score, compl_str = complete_line(st)
        return 0, score
    return cs[corupt_elem], 0


if __name__ == '__main__':
    with open(os.path.join('inputs', 'day10.txt'), 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda x: x.strip(), lines))

    print(sum([get_score(line)[0] for line in lines]))
    scores = list(filter(lambda x: x != 0, [get_score(line)[1] for line in lines]))
    print(sorted(scores)[len(scores) // 2])
