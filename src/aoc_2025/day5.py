from pathlib import Path

from intervaltree import Interval, IntervalTree

input_text = Path("input_data/day5.txt").read_text().strip().split("\n")


def parse_input(input_text):
    idx = []
    ingreds = []
    for line in input_text:
        if "-" in line:
            fields = line.split("-")
            idx.append((int(fields[0]), int(fields[1])))
        elif line:
            ingreds.append(int(line))
    return idx, ingreds


def part_1(idx, ingreds):
    cnt = 0
    for ingred in ingreds:
        for rng in idx:
            if rng[0] <= ingred <= rng[1]:
                cnt += 1
                break
    return cnt


idx, ingreds = parse_input(input_text)
print("Part 1:", part_1(idx, ingreds))


def part_2(idx):
    tree = IntervalTree(Interval(i[0], i[1] + 1) for i in idx)
    tree.merge_overlaps()
    return sum([(t.end - t.begin) for t in tree])


print("Part 2:", part_2(idx))
