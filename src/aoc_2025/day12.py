from pathlib import Path

import numpy as np

input_text = Path("input_data/day12.txt").read_text().split("\n")


def parse_text(input_text):
    shapes = []
    sub_shape = []
    grids = []
    counts = []
    for line in input_text:
        if not line:
            if sub_shape:
                shapes.append(np.array(sub_shape))
            sub_shape = []
        elif "#" in line:
            sub_shape.append([1 if i == "#" else 0 for i in line.strip()])
        elif "x" in line:
            fields = line.split(":")
            grids.append(tuple(map(int, fields[0].split("x"))))
            counts.append(tuple(map(int, fields[1].split())))
    return shapes, grids, counts


def part_1(grids, counts):
    return sum([g[0] * g[1] >= sum(c) * 9 for g, c in zip(grids, counts)])


shapes, grids, counts = parse_text(input_text)
print("Part 1:", part_1(grids, counts))
