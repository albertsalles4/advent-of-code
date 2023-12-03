from aocd import get_data

DAY, YEAR = 3, 2023


def is_part(data, i, j, n):
    l = j - len(n) if j - len(n) >= 0 else j - len(n) + 1
    r = j + 1 if j + 1 < len(data) else j
    u = i - 1 if i - 1 >= 0 else i
    d = i + 1 if i + 1 < len(data) else i

    for x in range(l, r + 1):
        for y in range(u, d + 1):
            if j - len(n) + 1 <= x <= j and y == i:
                continue
            if not data[y][x].isdigit() and data[y][x] != ".":
                return True, (y, x)

    return False, None


def part_a(data):
    s = 0
    for i, line in enumerate(data):
        j = 0
        while j < len(line):
            n = ""
            while j < len(line) and line[j].isdigit():
                n += line[j]
                j += 1
            if n and is_part(data, i, j - 1, n)[0]:
                s += int(n)
            j += 1
    return s


def part_b(data):
    gears = {}
    for i, line in enumerate(data):
        j = 0
        while j < len(line):
            n = ""
            while j < len(line) and line[j].isdigit():
                n += line[j]
                j += 1
            if n:
                is_p, p = is_part(data, i, j - 1, n)
                if is_p and data[p[0]][p[1]] == "*":
                    gears[p] = gears.get(p, []) + [int(n)]
            j += 1

    s = 0
    for p, l in gears.items():
        if len(l) == 2:
            s += l[0] * l[1]

    return s


aoc_data = get_data(day=DAY, year=YEAR).splitlines()
test_data = """\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".splitlines()

if __name__ == "__main__":
    assert part_a(test_data) == 4361
    assert part_b(test_data) == 467835
    print(part_a(aoc_data))
    print(part_b(aoc_data))
