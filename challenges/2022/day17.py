from aocd import get_data

DAY, YEAR = 17, 2022

ROCKS = [
    ["####"],
    [".#.", "###", ".#."],
    ["..#", "..#", "###"],
    ["#", "#", "#", "#"],
    ["##", "##"],
]


def contact(r1, p1, r2, p2):
    w1, h1 = len(r1[0]) - 1, len(r1) - 1
    w2, h2 = len(r2[0]) - 1, len(r2) - 1
    x1 = max(min(p1[0], p1[0] + w1), min(p2[0], p2[0] + w2))
    y1 = max(min(p1[1], p1[1] - h1), min(p2[1], p2[1] - h2))
    x2 = min(max(p1[0], p1[0] + w1), max(p2[0], p2[0] + w2))
    y2 = min(max(p1[1], p1[1] - h1), max(p2[1], p2[1] - h2))

    if x1 > x2 or y1 > y2:
        return False

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if r1[p1[1] - y][x - p1[0]] == "#" and r2[p2[1] - y][x - p2[0]] == "#":
                return True
    return False


def simulate_and_find_cycles(data, num_rocks, find_cycle=False):
    width, max_h = 7, 0
    stopped_rocks = {}
    gas = 0
    cache = [[] for _ in range(len(data))]
    loop_start = None
    loop_start_h = None
    loop_start_rock = None
    for rock_fall in range(num_rocks):
        rock = ROCKS[rock_fall % len(ROCKS)]
        x, y = 2, max_h + 3 + len(rock)
        moving = True
        moves = [max_h, rock_fall % len(ROCKS), gas]
        while moving:
            # jet of gas push
            if data[gas] == ">":
                cant_move = any(
                    contact(rock, (x + 1, y), ROCKS[r], (rx, ry))
                    for ry in range(y - len(rock), y + 4)
                    for r, rx in stopped_rocks.get(ry, [])
                )
                if x + len(rock[0]) < width and not cant_move:
                    x += 1
                    moves.append(">")
            elif data[gas] == "<":
                cant_move = any(
                    contact(rock, (x - 1, y), ROCKS[r], (rx, ry))
                    for ry in range(y - len(rock), y + 4)
                    for r, rx in stopped_rocks.get(ry, [])
                )
                if x - 1 >= 0 and not cant_move:
                    x -= 1
                    moves.append("<")
            gas = (gas + 1) % len(data)

            # fall
            cant_move = any(
                contact(rock, (x, y - 1), ROCKS[r], (rx, ry))
                for ry in range(y - len(rock) - 1, y + 3)
                for r, rx in stopped_rocks.get(ry, [])
            )
            if y - len(rock) == 0 or cant_move:
                moving = False
                if y in stopped_rocks:
                    stopped_rocks[y].append((rock_fall % len(ROCKS), x))
                else:
                    stopped_rocks[y] = [(rock_fall % len(ROCKS), x)]
                max_h = max(max_h, y)
                if find_cycle:
                    moves[0] = max_h - moves[0]
                    if loop_start is None and moves in cache[gas]:
                        loop_start = moves
                        loop_start_rock = rock_fall + 1
                        loop_start_h = max_h
                    elif loop_start is not None and loop_start == moves:
                        return loop_start_rock, loop_start_h, rock_fall + 1, max_h
                    cache[gas].append(moves)
            else:
                y -= 1
                moves.append("v")
    return max_h


def part_a(data):
    return simulate_and_find_cycles(data, 2022)


def part_b(data):
    n = 1000000000000
    ls, lh, r, h = simulate_and_find_cycles(data, n, find_cycle=True)
    loop = r - ls
    loop_h = h - lh
    remainder = (n - ls) % loop
    divider = (n - ls) // loop
    return simulate_and_find_cycles(data, ls + remainder) + loop_h * divider


aoc_data = get_data(day=DAY, year=YEAR)
test_data = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""

if __name__ == "__main__":
    assert part_a(test_data) == 3068
    assert part_b(test_data) == 1514285714288
    print(part_a(aoc_data))
    print(part_b(aoc_data))
