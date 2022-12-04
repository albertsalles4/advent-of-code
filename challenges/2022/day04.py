from aocd import get_data

DAY, YEAR = 4, 2022


def part_a(data):
    s = 0
    for line in data:
        p1, p2 = line.split(",")
        m1, M1 = [int(i) for i in p1.split("-")]
        m2, M2 = [int(i) for i in p2.split("-")]
        if (m1 <= m2 and M2 <= M1) or (m2 <= m1 and M1 <= M2):
            s += 1
    return s


def part_b(data):
    s = 0
    for line in data:
        p1, p2 = line.split(",")
        m1, M1 = [int(i) for i in p1.split("-")]
        m2, M2 = [int(i) for i in p2.split("-")]
        if m1 <= m2 <= M1 or m1 <= M2 <= M1 or m2 <= m1 <= M2 or m2 <= M1 <= M2:
            s += 1
    return s


aoc_data = get_data(day=DAY, year=YEAR).split("\n")
test_data = """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".split(
    "\n"
)

if __name__ == "__main__":
    assert part_a(test_data) == 2
    assert part_b(test_data) == 4
    print(part_a(aoc_data))
    print(part_b(aoc_data))
