from pathlib import Path

input_text = Path("input_data/day7.txt").read_text().split("\n")


def part_1(input_text):
    cnt = 0
    beam = [0] * (len(input_text[0]))
    beam[input_text[0].index("S")] = 1
    for row in input_text[1:]:
        for i, c in enumerate(row):
            if c == "^" and beam[i] > 0:
                beam[i - 1] += beam[i]
                beam[i + 1] += beam[i]
                beam[i] = 0
                cnt += 1

    return cnt, sum(beam)


p1, p2 = part_1(input_text)
print("Part 1:", p1)
print("Part 2:", p2)
