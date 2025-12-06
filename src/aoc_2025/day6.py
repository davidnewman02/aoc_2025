from pathlib import Path

import numpy as np

input_text = Path("input_data/day6.txt").read_text().split("\n")
if not input_text[-1]:
    input_text.pop(-1)


def parse_input(input_text):
    out = []
    for row in input_text:
        if "+" in row:
            ops = row.strip().split()
        elif row:
            out.append([int(i) for i in row.strip().split()])

    arr = np.array(out)
    return arr, ops


def accumulate(nums, op):
    if op == "+":
        return sum(nums)
    elif op == "*":
        return np.prod(nums)
    raise (ValueError(f"Unknown op: {op} {nums}"))


def part_1(arr, ops):
    cnt = 0
    for col, op in zip(arr.T, ops):
        cnt += accumulate(col, op)
    return cnt


arr, ops = parse_input(input_text)
print("Part 1:", part_1(arr, ops))


def part_2(input_text):
    cnt = 0
    nums = []
    for col in zip(*input_text):
        try:
            num = int("".join(col[:-1]))
            nums.append(num)
            if col[-1] != " ":
                op = col[-1]
        except ValueError:
            cnt += accumulate(nums, op)
            nums = []

    cnt += accumulate(nums, op)
    return cnt


arr, ops = parse_input(input_text)
print("Part 1:", part_1(arr, ops))
print("Part 2:", part_2(input_text))
