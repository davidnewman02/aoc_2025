import math
from pathlib import Path

input_text = Path("input_data/day1.txt").read_text().strip().split("\n")


## Part 1
total = 100
pos = 50
counter = 0

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

print("part 2:", counter)

#####################################
total = 100
pos = 50
counter = 0

for turn in input_text:
    dir = 1 if turn[0] == "R" else -1
    clicks = int(turn[1:])
    new_pos = pos + (dir * clicks)

    # Get the hundreds counter of the higher/lower position
    # and count hundreds between them 
    # e.g. 5-counts between (170, -320) 
    high_00s = (max(pos, new_pos) // total)
    low_00s = math.ceil(min(pos, new_pos) / total)
    count = high_00s - low_00s + 1 
    if not new_pos % total:
        count -= 1
    counter += count

    pos = new_pos

print("part 2:", counter, "(alternative formulation)")
