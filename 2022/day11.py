import os
from copy import deepcopy
from itertools import accumulate


class Monkey:

    def __init__(self, name, items, operation_fn, test_div, throw_to_false, throw_to_true, operator, operand):
        self.name = name
        self.test_div = test_div
        self.items = items
        self.operation_fn = operation_fn
        self.total_inspected = 0

        self.throw_to_false = throw_to_false
        self.throw_to_true = throw_to_true

        self.operator = operator
        self.operand = operand

    def throw_item(self, index: int, monkey):
        item = self.items[index]
        del self.items[index]
        monkey.catch_item(item)

    def catch_item(self, item):
        self.items.append(item)

    def op(self, item):
        if self.operator == "+":
            res = item + self.operand
            print(f"\t\t Worry level increases by {self.operand} to {res}")
            return res
        elif self.operator == "*":
            res = item * self.operand
            print(f"\t\t Worry level is multiplied by {self.operand} to {res}")
            return res
        raise ValueError()

    def inspect(self, throw_to_true, throw_to_false, divide=True, modullo=None):
        print(f"{self.name}:")
        index = 0
        while index < len(self.items):
            print(f"\t Monkey inspects an item with a worry level of {self.items[index]}")
            if self.operation_fn is not None:
                self.items[index] = self.operation_fn(self.items[index])
                print(f"\t\t Worry level is squarred to {self.items[index]}")
            else:
                self.items[index] = self.op(self.items[index])
            if divide:
                self.items[index] = self.items[index] // 3
                print(f"\t\t Monkey gets bored with item. Worry level is divided by 3 to {self.items[index]}")

            if modullo is not None:
                self.items[index] %= modullo
            if self.items[index] % self.test_div == 0:
                print(f"\t\t Current worry level is divisible by {self.test_div}")
                self.throw_item(index, throw_to_true)
            else:
                print(f"\t\t Current worry level is not divisible by {self.test_div}")
                self.throw_item(index, throw_to_false)

            self.total_inspected += 1


def p1(monkeys, d):
    for round in range(1, 21):
        print(f"Round {round}")
        for monkey in monkeys:
            monkey.inspect(throw_to_true=monkeys[monkey.throw_to_true],
                           throw_to_false=monkeys[monkey.throw_to_false],
                           divide=True, modullo=d)
        print("=" * 50)

        print(f"After round {round} monkeys are holding items with these worry levels:")
        for monkey in monkeys:
            print(f"Monkey {monkey.name}: {monkey.items}")

        print("=" * 50)

    for monkey in monkeys:
        print(f"Monkey {monkey.name} inspected items {monkey.total_inspected} times")

    print(list(accumulate(sorted(list(map(lambda x: x.total_inspected, monkeys)))[-2:], (lambda x, y: x * y)))[-1])


def p2(monkeys, d):
    for round in range(1, 10001):
        for monkey in monkeys:
            monkey.inspect(throw_to_true=monkeys[monkey.throw_to_true],
                           throw_to_false=monkeys[monkey.throw_to_false],
                           divide=False, modullo=d)
    for monkey in monkeys:
        print(f"Monkey {monkey.name} inspected items {monkey.total_inspected} times")

    print(list(accumulate(sorted(list(map(lambda x: x.total_inspected, monkeys)))[-2:], (lambda x, y: x * y)))[-1])


if __name__ == '__main__':
    with open(os.path.join('inputs', 'day11.txt'), 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda x: x.strip(), lines)) + [""]
    monkeys = []
    items, operation_fn, test_div, throw_to_false, throw_to_true, operator, operand = None, None, None, None, None, None, None
    ind = 0
    d = 1
    for line in lines:
        if line == "":
            monkeys.append(
                Monkey(f"Monkey {ind}", items, operation_fn, test_div, throw_to_false, throw_to_true, operator,
                       operand))
            ind += 1
            items, operation_fn, test_div, throw_to_false, throw_to_true, operator, operand = None, None, None, None, None, None, None
        elif "Starting items" in line:
            items = list(map(int, line.split(":")[1].split(",")))
        elif "Operation" in line:
            op = line.split(":")[1].split("= ")[1]
            if op == "old * old":
                operation_fn = lambda old: old * old
            elif "*" in op:
                operator = "*"
                operand = int(op.split("* ")[1])
            elif "+" in op:
                operator = "+"
                operand = int(op.split("+ ")[1])

        elif "Test" in line:
            test_div = int(line.split(":")[1].split("by ")[1])
            d *= test_div
        elif "If true" in line:
            throw_to_true = int(line.split(":")[1].split("monkey ")[1])
        elif "If false" in line:
            throw_to_false = int(line.split(":")[1].split("monkey ")[1])

    p1(deepcopy(monkeys), d)
    p2(deepcopy(monkeys), d)
