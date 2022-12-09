from aocd import get_data

DAY, YEAR = 9, 2022


def move_tail(head, tail):
    if max(abs(head[0] - tail[0]), abs(head[1] - tail[1])) > 1:
        if head[0] != tail[0]:
            tail[0] += 1 if head[0] > tail[0] else -1
        if head[1] != tail[1]:
            tail[1] += 1 if head[1] > tail[1] else -1
    return tail


def move_head(move, head):
    if move == "U":
        head[1] += 1
    elif move == "D":
        head[1] -= 1
    elif move == "L":
        head[0] -= 1
    elif move == "R":
        head[0] += 1
    return head


def part_a(data):
    grid = set()
    (xh, yh), (xt, yt) = (0, 0), (0, 0)

    for line in data:
        mv, n = line.split(" ")
        for _ in range(int(n)):
            (xh, yh) = move_head(mv, [xh, yh])
            (xt, yt) = move_tail([xh, yh], [xt, yt])
            grid.add((xt, yt))
    return len(grid)


def part_b(data):
    grid = set()
    rope = [[0, 0] for _ in range(10)]

    for line in data:
        mv, n = line.split(" ")
        for _ in range(int(n)):
            rope[0] = move_head(mv, rope[0])
            for i in range(1, len(rope)):
                rope[i] = move_tail(rope[i - 1], rope[i])
            grid.add((rope[-1][0], rope[-1][1]))
    return len(grid)


aoc_data = get_data(day=DAY, year=YEAR).splitlines()
test_data = """\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".splitlines()

test_data2 = """\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""".splitlines()

if __name__ == "__main__":
    assert part_a(test_data) == 13
    assert part_b(test_data2) == 36
    print(part_a(aoc_data))
    print(part_b(aoc_data))
