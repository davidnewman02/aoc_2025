import itertools
import math
from pathlib import Path

import numpy as np


def parse_coords(input_text):
    coords = []
    for line in input_text:
        coords.append(tuple(map(int, line.split(","))))
    return coords

def conn_list(coords):
    dists = {}
    for i in range(len(coords) - 1):
        for j in range(i + 1, len(coords) - 1):
            dists[(i, j)] = math.dist(coords[i], coords[j])
    return sorted(dists, key=dists.get)


def part_2(input_text, num_pairs, num_nets):
    coords = parse_coords(input_text)
    idxs = conn_list(coords)

    nets = []
    for i, idx in enumerate(idxs):
        merge = set()
        pop_idx = []
        for j, n in enumerate(nets):
            if idx[0] in n or idx[1] in n:
                merge.update(idx)
                merge.update(n)
                pop_idx.append(j)

        if not merge:
            nets.append(set(idx))
        else:
            [nets.pop(j) for j in pop_idx[::-1]]
            nets.append(merge)

        if i == num_pairs:
            p1 = np.prod(sorted([len(i) for i in nets])[-num_nets:])

        if len(nets) == 1 and len(nets[0]) >= (len(input_text) - 1):
            break

    p2 = coords[idx[0]][0] * coords[idx[1]][0]
    return p1, p2


input_text = Path("input_data/day8.txt").read_text().strip().split("\n")
coords = parse_coords(input_text)
p1, p2 = part_2(input_text, num_pairs=1000, num_nets=3)
print("Part 1:", p1)
print("Part 2:", p2)
