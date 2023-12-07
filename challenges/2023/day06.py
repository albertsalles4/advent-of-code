from aocd import get_data

DAY, YEAR = 6, 2023


def parse(data):
    time = map(int, data[0].split(':')[1].split())
    dist = map(int, data[1].split(':')[1].split())
    return time, dist


def part_a(data):
    time, dist = parse(data)

    res = 1
    for t, d in zip(time, dist):
        m = next(i for i in range(t) if i * (t - i) > d)
        res *= t - 2*m + 1
    return res


def part_b(data):
    time, dist = parse(data)

    t = int("".join([str(ti) for ti in time]))
    d = int("".join([str(di) for di in dist]))
    m = next(i for i in range(t) if i * (t - i) > d)
    return t - 2*m + 1


aoc_data = get_data(day=DAY, year=YEAR).splitlines()
test_data = """\
Time:      7  15   30
Distance:  9  40  200
""".splitlines()

if __name__ == "__main__":
    assert part_a(test_data) == 288
    assert part_b(test_data) == 71503
    print(part_a(aoc_data))
    print(part_b(aoc_data))
