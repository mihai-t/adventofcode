import os


def find_double_points(lines, only_horiz):
    points = set()
    at_least_once = set()
    for line in lines:
        x1, y1, x2, y2 = line
        if only_horiz and (x1 != x2 and y1 != y2):
            continue
        if x1 == x2:
            st, en = min(y1, y2), max(y1, y2)
            for y in range(st, en + 1):
                pt = (x1, y)
                if pt in points:
                    if pt in at_least_once:
                        continue
                    at_least_once.add(pt)
                else:
                    points.add(pt)
        elif y1 == y2:
            st, en = min(x1, x2), max(x1, x2)
            for x in range(st, en + 1):
                pt = (x, y1)
                if pt in points:
                    if pt in at_least_once:
                        continue
                    at_least_once.add(pt)
                else:
                    points.add(pt)
        else:  # diagonal
            if x1 < x2:
                stx, sty, enx, eny = x1, y1, x2, y2
            else:
                stx, sty, enx, eny = x2, y2, x1, y1

            x, y = stx, sty
            while x <= enx:
                pt = (x, y)
                x += 1
                if y <= eny:
                    y += 1
                else:
                    y -= 1
                if pt in points:
                    if pt in at_least_once:
                        continue
                    at_least_once.add(pt)
                else:
                    points.add(pt)

    print(len(at_least_once))


if __name__ == '__main__':
    with open(os.path.join('inputs', 'day5.txt'), 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda x: x.split('->'), lines))
        lines = list(map(lambda x: (
            (int(x[0].split(',')[0]), int(x[0].split(',')[1]), int(x[1].split(',')[0]), int(x[1].split(',')[1]))),
                         lines))

    find_double_points(lines, only_horiz=True)
    find_double_points(lines, only_horiz=False)
