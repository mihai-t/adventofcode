import os
from copy import deepcopy
from functools import reduce


def get_version_and_type_id(binary, start_position):
    if not binary[start_position:start_position + 3]:
        return -1, -1, start_position + 6
    version = int(binary[start_position:start_position + 3], 2)
    if not binary[start_position + 3:start_position + 6]:
        return version, -1, start_position + 6
    type_id = int(binary[start_position + 3:start_position + 6], 2)
    return version, type_id, start_position + 6


def get_literal(binary, start_position):
    num = ''
    for i in range(start_position, len(binary), 5):

        num += binary[i + 1:i + 5]

        if binary[i] == '0':
            break
    return num, i + 5


def get_operator(type_id):
    if type_id == 0:
        return '+'
    if type_id == 1:
        return '*'
    if type_id == 2:
        return 'min'
    if type_id == 3:
        return 'max'
    if type_id == 5:
        return '>'
    if type_id == 6:
        return '<'
    if type_id == 7:
        return '='

    raise ValueError(type_id)


def do_operation(op, nums):
    if op == 'min':
        print(op, nums, min(nums))
        return min(nums)
    elif op == 'max':
        print(op, nums, max(nums))
        return max(nums)
    elif op == '+':
        print(op, nums, sum(nums))
        return sum(nums)
    elif op == '*':
        print(op, nums, reduce(lambda x, y: x * y, nums, 1))
        return reduce(lambda x, y: x * y, nums, 1)
    elif op == '<':
        print(op, nums, 1 if nums[0] < nums[1] else 0)
        return 1 if nums[0] < nums[1] else 0
    elif op == '>':
        print(op, nums, 1 if nums[0] > nums[1] else 0)
        return 1 if nums[0] > nums[1] else 0
    elif op == '=':
        print(op, nums, 1 if nums[0] == nums[1] else 0)
        return 1 if nums[0] == nums[1] else 0
    else:
        raise ValueError(op)


def parse_operator(binary, start_position, all_nums, all_versions):
    if start_position >= len(binary):
        return start_position, all_nums, all_versions
    length_type_id = binary[start_position]
    start_position += 1
    if length_type_id == '0':
        ln = binary[start_position:start_position + 15]
        if not ln:
            return start_position, all_nums, all_versions
        ln = int(ln, 2)
        start_position += 15
        total_ln = 0  # version and type id
        while ln - total_ln > 3:
            version, type_id, start_position = get_version_and_type_id(binary, start_position)
            if version == -1:
                break
            all_versions.append(version)
            total_ln += 6
            if type_id == -1:
                break
            elif type_id == 4:
                num, start_position = get_literal(binary, start_position)
                total_ln += len(num)
                all_nums.append(int(num, 2))
            else:
                op = get_operator(type_id)
                all_nums_so_far = deepcopy(all_nums)
                start_position, all_nums, all_versions = parse_operator(binary, start_position, all_nums, all_versions)
                all_nums = all_nums_so_far + [do_operation(op, all_nums[len(all_nums_so_far):])]
                print(all_nums)
    else:
        num_sub_packets = int(binary[start_position:start_position + 11], 2)
        start_position += 11
        for _ in range(num_sub_packets):
            version, type_id, start_position = get_version_and_type_id(binary, start_position)
            all_versions.append(version)
            if type_id == -1:
                break
            elif type_id == 4:
                num, start_position = get_literal(binary, start_position)
                all_nums.append(int(num, 2))
            else:
                op = get_operator(type_id)
                all_nums_so_far = deepcopy(all_nums)
                start_position, all_nums, all_versions = parse_operator(binary, start_position, all_nums, all_versions)
                all_nums = all_nums_so_far + [do_operation(op, all_nums[len(all_nums_so_far):])]
                print(all_nums)
    return start_position, all_nums, all_versions


if __name__ == '__main__':
    with open(os.path.join('inputs', 'day16.txt'), 'r') as f:
        lines = f.readlines()
        hex_data = lines[0]

    start_position = 0
    num_of_bits = len(hex_data) * 4
    binary = bin(int(hex_data, 16))[2:].zfill(num_of_bits)
    version, type_id, start_position = get_version_and_type_id(binary, start_position)
    all_versions = [version]

    if type_id == 4:
        num, end_position = get_literal(binary, start_position)
        all_nums = [int(num, 2)]
    else:  # other than 4 operator
        op = get_operator(type_id)
        _, all_nums, all_versions = parse_operator(binary, start_position, [], all_versions)
        print("versions", all_versions, sum(all_versions))
        print(do_operation(op, all_nums))
    assert sum(all_versions) == 969
    # print(all_nums)

    # 95562857 too low
    # 95562845 too low
