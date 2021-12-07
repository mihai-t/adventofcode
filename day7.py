import os

if __name__ == '__main__':
    with open(os.path.join('inputs', 'day7.txt'), 'r') as f:
        lines = f.readlines()
        numbers = list(map(int, lines[0].split(',')))

    pos = sorted(numbers)[len(numbers) // 2]
    total = sum([abs(pos - n) for n in numbers])
    print(pos, total)

    pos = int(sum(numbers) / len(numbers))
    total = sum([(abs(pos - n) * (abs(pos - n) + 1)) // 2 for n in numbers])
    print(pos, total)