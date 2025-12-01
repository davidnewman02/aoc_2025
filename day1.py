from pathlib import Path

input_text = Path("input_data/day1.txt").read_text().split("\n")


total = 100
pos = 50
counter = 0

## Part 1
for turn in input_text:
    dir = 1 if turn[0] == "R" else -1
    clicks = int(turn[1:])
    pos = (pos + dir * clicks) % total
    # print(turn, dir*clicks, pos)

    if pos == 0:
        counter += 1

print("part 1: ", counter)


## Part 2
total = 100
pos = 50
counter = 0

for turn in input_text:

    dir = 1 if turn[0] == "R" else -1
    clicks = int(turn[1:])

    counter += clicks // total
    clicks %= total

    if pos == 0 and dir == -1:
        counter -= 1

    pos += dir * clicks

    if not 0 < pos < total:
        counter += 1
        pos %= total

print("part 2: ", counter)
