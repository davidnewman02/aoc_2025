import functools
import itertools
from pathlib import Path

import numpy as np
import pulp

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
    for presses in range(1, len(s)):
        for cmb in itertools.combinations(s, presses):
            result = functools.reduce(np.bitwise_xor, cmb)
            if np.array_equal(result, l):
                return presses
    return len(s)


def part_1(machines):
    return sum([check_combos(l, s) for l, s, _ in machines])


def part_2(machines):
    cnt = 0
    for _, switches, jolts in machines:

        buttons = np.array(switches, dtype=int)
        n_switches, n_lights = buttons.shape

        # Set up solver and variables
        prob = pulp.LpProblem("find_presses", pulp.LpMinimize)
        x = pulp.LpVariable.dicts("x", range(n_switches), lowBound=0, cat="Integer")
        prob += pulp.lpSum(x[j] for j in range(n_switches))

        # For each light, the sum of contributions from all switches must match its joltage target.
        # Add these as target constraints
        for i in range(n_lights):
            prob += (
                pulp.lpSum(buttons[j, i] * x[j] for j in range(n_switches)) == jolts[i]
            )

        prob.solve(pulp.PULP_CBC_CMD(msg=False))
        presses = sum([pulp.value(x[j]) for j in range(n_switches)])
        cnt += presses
    return int(cnt)


machines = parse_text(input_text)
print("Part 1:", part_1(machines))
print("Part 2:", part_2(machines))
