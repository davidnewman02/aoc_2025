from pathlib import Path

input_text = Path("input_data/day3.txt").read_text().strip().split("\n")


def part_1(input_text):
    cnt = 0
    for bank in input_text:
        bank = [int(i) for i in bank]
        dig_1 = max(bank[:-1])
        dig_2 = max(bank[bank.index(dig_1) + 1 :])
        cnt += dig_1 * 10 + dig_2
    return cnt


print("Part 1:", part_1(input_text))


def get_joltage(bank):
    nbatt = 12
    nskip = len(bank) - nbatt
    out_num = ""

    while len(out_num) < 12:
        dig_1 = max(bank[: nskip + 1])
        out_num += str(dig_1)
        pos = bank.index(dig_1)
        nskip -= pos
        bank = bank[pos + 1 :]
    return int(out_num)


def part_2(input_text):
    cnt = 0
    for bank in input_text:
        bank = [int(i) for i in bank]
        jolt = get_joltage(bank)
        cnt += jolt

    return cnt


print("Part 2:", part_2(input_text))
