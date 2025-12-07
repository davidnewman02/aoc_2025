import numpy as np
from pathlib import Path

input_text = Path("input_data/day4.ex.txt").read_text().strip().split("\n")


def parse_input(input_text):
    out = []
    for i in input_text:
        out.append([1 if l == "@" else 0 for l in i])
    arr = np.array(out)

    return arr


def get_neighbours(arr, pos):
    a, b = pos
    r0 = max(a - 1, 0)
    r1 = min(a + 2, arr.shape[0])
    c0 = max(b - 1, 0)
    c1 = min(b + 2, arr.shape[1])
    return arr[r0:r1, c0:c1]


def part_1(arr):
    cnt = 0
    for pos in np.argwhere(arr == 1):
        neighbours = get_neighbours(arr, pos)
        if neighbours.sum() <= 4:
            cnt += 1
    return cnt


input_arr = parse_input(input_text)
print("Part 1:", part_1(input_arr))


def clear_rolls(arr):
    for pos in np.argwhere(arr == 1):
        if not arr[*pos] == 1:
            continue
        neighbours = get_neighbours(arr, pos)
        if neighbours.sum() <= 4:
            arr[*pos] = 0
    return arr


def part_2(arr):
    initial_total = arr.sum()
    prev_cnt = arr.sum()
    while True:
        arr = clear_rolls(arr)
        if arr.sum() == prev_cnt:
            return initial_total - arr.sum()
        prev_cnt = arr.sum()


print("Part 2:", part_2(input_arr))
