import functools
import itertools
from pathlib import Path

import numpy as np

input_text = Path("input_data/day10.txt").read_text().split("\n")


def parse_text(input_text):
    machines = []
    jolts = []
    for line in input_text:
        if not line:
            continue
        fields = line.split(" ")
        lights = np.array([1 if i == "#" else 0 for i in fields[0][1:-1]])
        switches = []
        for switch in fields[1:-1]:
            s = np.zeros(len(lights), dtype=bool)
            s[[int(i) for i in switch[1:-1].split(",")]] = True
            switches.append(s)
        jolts = [int(i) for i in fields[-1][1:-1].split(",")]

        machines.append((lights, switches, jolts))
    return machines


def check_combos(l, s):
    for i in range(1, len(s)):
        for cmb in itertools.combinations(s, i):
            result = functools.reduce(np.bitwise_xor, cmb)
            if np.array_equal(result, l):
                return i
    return len(s)


def part_1(machines):
    cnt = 0
    for l, s, _ in machines:
        count = check_combos(l, s)
        cnt += count
    return cnt


machines = parse_text(input_text)

print("Part 1:", part_1(machines))
