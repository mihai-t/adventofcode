import os


def day(fishes):
    new_count = {}
    for f, cnt in fishes.items():
        f -= 1
        if f == -1:
            new_count[8] = new_count.get(8, 0) + cnt
            new_count[6] = new_count.get(6, 0) + cnt
        else:
            new_count[f] = new_count.get(f, 0) + cnt
    return new_count


if __name__ == '__main__':
    fishes = {}
    with open(os.path.join('inputs', 'day6.txt'), 'r') as f:
        lines = f.readlines()
        lines = list(map(int, lines[0].split(',')))
        for f in lines:
            fishes[f] = fishes.get(f, 0) + 1

    for d in range(1, 257):
        fishes = day(fishes)
        print('After', d, 'days: ', sum(fishes.values()))
