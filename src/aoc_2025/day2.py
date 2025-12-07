from pathlib import Path

input_text = Path("input_data/day2.ex.txt").read_text().strip().split(",")


def part_1(input_text):
    cnt = 0
    for line in input_text:
        start = int(line.split("-")[0])
        end = int(line.split("-")[1])
        for i in range(start, end + 1):
            i = str(i)
            if i[: len(i) // 2] == i[len(i) // 2 :]:
                cnt += int(i)

    return cnt


print("Part 1:", part_1(input_text))


def is_valid(i):
    for end in range(1, (len(i) // 2) + 1):
        if not len(i) % end:
            if i[:end] * (len(i) // end) == i:
                return True
    return False


def part_2(input_text):
    cnt = 0
    for line in input_text:
        start = int(line.split("-")[0])
        end = int(line.split("-")[1])
        for i in range(start, end + 1):
            if is_valid(str(i)):
                cnt += i
    return cnt


print("Part 2:", part_2(input_text))
