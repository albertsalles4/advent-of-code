from aocd import get_data

DAY, YEAR = 8, 2023


def parse_data(data):
    instructions = data[0]
    nodes = {}
    for line in data[2:]:
        n, lr = line.split(" = ")
        nodes[n] = lr[1:-1].split(", ")
    return instructions, nodes


def part_a(data):
    instructions, nodes = parse_data(data)
    n = "AAA"
    i = 0
    while n != "ZZZ":
        inst = instructions[i % len(instructions)]
        if inst == "L":
            n = nodes[n][0]
        else:
            n = nodes[n][1]

        i += 1
    return i


def part_b(data):
    instructions, nodes = parse_data(data)
    ns = [node for node in nodes if node.endswith("A")]

    cycles = {}
    for n in ns:
        i = 0
        while not n.endswith("Z"):
            inst = instructions[i % len(instructions)]
            if inst == "L":
                n = nodes[n][0]
            else:
                n = nodes[n][1]

            i += 1
        cycles[n] = i

    # Least common multiple
    from math import lcm
    from functools import reduce

    return reduce(lcm, cycles.values())


aoc_data = get_data(day=DAY, year=YEAR).splitlines()
test_data = """\
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
""".splitlines()

test_data2 = """\
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
""".splitlines()

if __name__ == "__main__":
    assert part_a(test_data) == 2
    assert part_b(test_data2) == 6
    print(part_a(aoc_data))
    print(part_b(aoc_data))
