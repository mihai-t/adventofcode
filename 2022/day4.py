import os

if __name__ == '__main__':
    with open(os.path.join('inputs', 'day4.txt'), 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda x: x.strip(), lines))

    ovr = 0
    ovr2 = 0
    for ln in lines:
        e1, e2 = ln.split(",")
        e11, e12 = tuple(map(int, e1.split("-")))
        e21, e22 = tuple(map(int, e2.split("-")))

        if (e11 <= e21 and e12 >= e22) or (e11 >= e21 and e12 <= e22):
            ovr += 1

        if (e11 <= e21 <= e12) or (e11 <= e22 <= e12) or (e21 <= e11 <= e22) or (e21 <= e12 <= e22):
            ovr2 += 1

    print(ovr)
    print(ovr2)
