from aocd import get_data

DAY, YEAR = 15, 2022


def parse_input(data):
    sensors = []
    beacons = []
    for line in data:
        s, b = line.split(": ")
        sensors.append(
            [int(s[s.index("x=") + 2 : s.index(",")]), int(s[s.index("y=") + 2 :])]
        )
        beacons.append(
            [int(b[b.index("x=") + 2 : b.index(",")]), int(b[b.index("y=") + 2 :])]
        )
    return sensors, beacons


def part_a(data, y=10):
    sensors, beacons = parse_input(data)
    row_y = set()
    by = set()
    for s, b in zip(sensors, beacons):
        dy = abs(s[0] - b[0]) + abs(s[1] - b[1]) - abs(y - s[1])
        for i in range(dy + 1):
            row_y.add(s[0] + i)
            row_y.add(s[0] - i)
        if b[1] == y and abs(b[0] - s[0]) <= dy:
            by.add(b[0])
    return len(row_y) - len(by)


def part_b(data, mc=20):
    sensors, beacons = parse_input(data)
    diagonals = [[], []]
    for s, b in zip(sensors, beacons):
        d = abs(s[0] - b[0]) + abs(s[1] - b[1])
        diagonals[0].append(s[1] - (s[0] - d))
        diagonals[0].append(s[1] - (s[0] + d))
        diagonals[1].append(s[1] + (s[0] - d))
        diagonals[1].append(s[1] + (s[0] + d))

    diagonals = [sorted(diagonals[0]), sorted(diagonals[1])]
    p0 = set(d for d in diagonals[0] if d + 2 in diagonals[0])
    p1 = set(d for d in diagonals[1] if d + 2 in diagonals[1])

    candidates = []
    for d0 in p0:
        for d1 in p1:
            x = (d1 - d0) // 2
            y = d0 + x
            if 0 <= x <= mc and 0 <= y + 1 <= mc:
                candidates.append([x, y + 1])
    for c in candidates:
        if all(
            abs(s[0] - b[0]) + abs(s[1] - b[1]) < abs(s[0] - c[0]) + abs(s[1] - c[1])
            for s, b in zip(sensors, beacons)
        ):
            return c[0] * 4000000 + c[1]
    return -1


aoc_data = get_data(day=DAY, year=YEAR).splitlines()
test_data = """\
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""".splitlines()

if __name__ == "__main__":
    assert part_a(test_data) == 26
    assert part_b(test_data) == 56000011
    print(part_a(aoc_data, y=2000000))
    print(part_b(aoc_data, mc=4000000))
