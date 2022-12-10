from aocd import get_data

DAY, YEAR = 10, 2022


def simulate(data):
    addx = [0] * 250
    addx[0] = 1
    i = 0
    for line in data:
        if line == "noop":
            i += 1
            continue
        n = int(line.split(" ")[1])
        i += 2
        if i > len(addx):
            break
        addx[i] = n

    for i in range(1, len(addx)):
        addx[i] += addx[i - 1]

    return addx


def part_a(data):
    addx = simulate(data)
    return sum(addx[i - 1] * i for i in range(20, 250, 40))


def part_b(data):
    addx = simulate(data)
    for i in range(40, 250, 40):
        draw = ""
        for j in range(40):
            if abs(j - addx[i - 40 : i][j]) < 2:
                draw += "#"
            else:
                draw += " "
        print(draw)


aoc_data = get_data(day=DAY, year=YEAR).splitlines()
test_data = """\
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop""".splitlines()

if __name__ == "__main__":
    assert part_a(test_data) == 13140
    assert part_b(test_data) is None
    print(part_a(aoc_data))
    print(part_b(aoc_data))
