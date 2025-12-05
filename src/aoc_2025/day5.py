from pathlib import Path

from intervaltree import Interval, IntervalTree

input_text = Path("input_data/day5.txt").read_text().strip().split("\n")


def parse_input(input_text):
    idx = []
    ingreds = []
    for line in input_text:
        if "-" in line:
            fields = line.split("-")
            idx.append(Interval(int(fields[0]), int(fields[1]) + 1))
        elif line:
            ingreds.append(int(line))
    tree = IntervalTree(idx)
    tree.merge_overlaps()
    return tree, ingreds


def part_1(tree, ingreds):
    return sum([1 if tree[i] else 0 for i in ingreds])


def part_2(tree):
    return sum([(t.end - t.begin) for t in tree])


tree, ingreds = parse_input(input_text)
print("Part 1:", part_1(tree, ingreds))
print("Part 2:", part_2(tree))
