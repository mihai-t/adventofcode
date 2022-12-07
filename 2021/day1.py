import os

if __name__ == '__main__':
    with open(os.path.join('inputs', 'day1.txt')) as f:
        numbers = list(map(int, f.readlines()))
    increase = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            increase += 1
    print('part 1', increase)
    increase = 0
    for i in range(1, len(numbers) - 2):
        a = sum(numbers[i - 1:i + 2])
        b = sum(numbers[i:i + 3])
        if b > a:
            increase += 1
    print('part 2', increase)
