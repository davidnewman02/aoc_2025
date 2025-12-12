from pathlib import Path

input_text = Path("input_data/day11.txt").read_text().split("\n")


def parse_text(input_text):
    net = {}
    for line in input_text:
        if not line:
            continue
        fields = line.split()
        net[fields[0][:-1]] = fields[1:]
    return net


def part_1(net, start="you", target="out"):
    memo = {}

    def search(node):
        if node == target:
            return 1
        elif node in memo:
            return memo[node]

        memo[node] = sum(search(child) for child in net[node])

        return memo[node]

    res = search(start)
    return res


net = parse_text(input_text)
print("Part 1:", part_1(net))


def part_2(net, start="you", target="out"):
    memo = {}

    def search(node, seen_fft, seen_dac):
        if node == "fft":
            seen_fft = True
        if node == "dac":
            seen_dac = True
        if node == target:
            if seen_fft and seen_dac:
                return 1
            return 0
        elif (node, seen_fft, seen_dac) in memo:
            return memo[(node, seen_fft, seen_dac)]

        memo[(node, seen_fft, seen_dac)] = sum(
            search(child, seen_fft, seen_dac) for child in net[node]
        )

        return memo[(node, seen_fft, seen_dac)]

    res = search(start, seen_fft=False, seen_dac=False)
    return res


print("Part 2:", part_2(net, start="svr"))
