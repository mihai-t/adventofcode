import os

if __name__ == '__main__':
    elfs = []
    with open(os.path.join('inputs', 'day1.txt')) as f:
        s = 0
        for ln in f.readlines():
            ln = ln.strip()
            if ln:
                s += int(ln)
            else:
                elfs.append(s)
                s = 0
    print(max(elfs))

    print(sum(sorted(elfs)[-3:]))
