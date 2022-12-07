import os


def count_bits(position, lines):
    count = {}
    for l in lines:
        bit = l[position]
        count[bit] = count.get(bit, 0) + 1
    return count


if __name__ == '__main__':
    with open(os.path.join('inputs', 'day3.txt')) as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
    g, e = '', ''
    ox, co = lines.copy(), lines.copy()
    final_ox, final_co = None, None
    for pos in range(0, len(lines[0])):
        c = count_bits(pos, lines)
        if c['0'] > c['1']:
            g += '0'
            e += '1'

        else:
            g += '1'
            e += '0'

        c1 = count_bits(pos, ox)
        if c1.get('0', 0) > c1.get('1', 0):
            ox = list(filter(lambda x: x[pos] == '0', ox))
        else:
            ox = list(filter(lambda x: x[pos] == '1', ox))

        c2 = count_bits(pos, co)
        if c2.get('0', 0) > c2.get('1', 0):
            co = list(filter(lambda x: x[pos] == '1', co))
        else:
            co = list(filter(lambda x: x[pos] == '0', co))

        if len(ox) == 1:
            final_ox = ox[0]
        if len(co) == 1:
            final_co = co[0]

    print(g, e)
    g = int(g, 2)
    e = int(e, 2)
    print('part 1', g, e, g * e)

    print(final_co, final_ox)
    final_co = int(final_co, 2)
    final_ox = int(final_ox, 2)
    print('part 2', final_ox, final_co, final_ox * final_co)
