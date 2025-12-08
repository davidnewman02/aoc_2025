import itertools
import math
from pathlib import Path

import numpy as np


def parse_coords(input_text):
    coords = []
    for line in input_text:
        coords.append(tuple(map(int, line.split(","))))
    return coords


def dist(a, b):
    return math.sqrt(sum((ai - bi) ** 2 for ai, bi in zip(a, b)))


def dist_list(coords):
    dists = {}
    for i in range(len(coords) - 1):
        for j in range(i + 1, len(coords) - 1):
            dists[(i, j)] = math.dist(coords[i], coords[j])
    return dists


def part_1(input_text, num_pairs, num_nets=3):
    coords = parse_coords(input_text)
    dists = dist_list(coords)

    nets = []
    for idx, _ in sorted(dists.items(), key=lambda x: x[1])[: num_pairs - 1]:
        merge = set()
        pop_idx = []
        for i, n in enumerate(nets):
            if idx[0] in n or idx[1] in n:
                merge.update(idx)
                merge.update(n)
                pop_idx.append(i)

        if not merge:
            nets.append(set(idx))
        else:
            [nets.pop(i) for i in pop_idx[::-1]]
            nets.append(merge)

    score = np.prod(sorted([len(i) for i in nets])[-num_nets:])
    return score


# input_text = Path("input_data/day8.ex.txt").read_text().strip().split("\n")
# pairs = 10
# num_nets = 3
# print("Part 1 ex:", part_1(input_text, pairs, num_nets))

input_text = Path("input_data/day8.txt").read_text().strip().split("\n")
pairs = 1000
num_nets = 3
print("Part 1:", part_1(input_text, pairs, num_nets))


def part_2(input_text):
    coords = parse_coords(input_text)
    dists = dist_list(coords)

    nets = []
    for idx, _ in sorted(dists.items(), key=lambda x: x[1]):
        merge = set()
        pop_idx = []
        for i, n in enumerate(nets):
            if idx[0] in n or idx[1] in n:
                merge.update(idx)
                merge.update(n)
                pop_idx.append(i)

        if not merge:
            nets.append(set(idx))
        else:
            [nets.pop(i) for i in pop_idx[::-1]]
            nets.append(merge)

        if len(nets) == 1 and len(nets[0]) >= (len(input_text) - 1):
            break

    return coords[idx[0]][0] * coords[idx[1]][0]


input_text = Path("input_data/day8.txt").read_text().strip().split("\n")
coords = parse_coords(input_text)
print("Part 2", part_2(input_text))
