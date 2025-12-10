import itertools
from pathlib import Path

input_text = Path("input_data/day9.txt").read_text().split("\n")
if not input_text[-1]:
    input_text.pop(-1)


def part_1(input_text):
    p1_area = 0
    p2_area = 0
    coords = [tuple(map(int, line.split(","))) for line in input_text]
    edges = list(zip(coords, coords[1:] + [coords[0]]))
    v_edges = [
        (x0, min(y0, y1), max(y0, y1)) for (x0, y0), (x1, y1) in edges if x0 == x1
    ]
    h_edges = [
        (y0, min(x0, x1), max(x0, x1)) for (x0, y0), (x1, y1) in edges if y0 == y1
    ]

    for (x0, y0), (x1, y1) in itertools.combinations(coords, 2):
        area = (abs(x0 - x1) + 1) * (abs(y0 - y1) + 1)
        p1_area = max(p1_area, area)
        if p2_area > area:
            # No need to check if it's already smaller than max
            continue

        contained = True
        min_x, max_x = min(x0, x1) + 0.5, max(x0, x1) - 0.5
        min_y, max_y = min(y0, y1) + 0.5, max(y0, y1) - 0.5

        for v_x, min_v_y, max_v_y in v_edges:
            ve_in_x = min_x < v_x < max_x
            yends = min_v_y < min_y < max_v_y or min_v_y < max_y < max_v_y
            if ve_in_x and yends:
                contained = False
                break

        if contained:
            for h_y, min_h_x, max_h_x in h_edges:
                he_in_y = min_y < h_y < max_y
                xends = min_h_x < min_x < max_h_x or min_h_x < max_x < max_h_x

                if he_in_y and xends:
                    contained = False
                    break
        if contained:
            p2_area = area

    return p1_area, p2_area


p1, p2 = part_1(input_text)
print("Part 1:", p1)
print("Part 2:", p2)
