from aocd import get_data

DAY, YEAR = 24, 2022


def parse_data(data):
    rows = [[] for _ in range(len(data) - 2)]
    cols = [[] for _ in range(len(data[0]) - 2)]

    for i in range(1, len(data) - 1):
        for j in range(1, len(data[i]) - 1):
            if data[i][j] in ["<", ">"]:
                rows[i - 1].append((j - 1, 1 if data[i][j] == ">" else -1))
            elif data[i][j] in ["^", "v"]:
                cols[j - 1].append((i - 1, 1 if data[i][j] == "v" else -1))
    return rows, cols


def find_path(rows, cols, start, end, initial_time=0):
    pos = start
    visited = {}
    candidates = [(pos, initial_time)]
    shortest_path = None
    while candidates:
        pos, steps = candidates.pop(-1)
        min_steps_required = steps + abs(pos[0] - end[0]) + abs(pos[1] - end[1])
        if shortest_path is not None and min_steps_required > shortest_path:
            continue
        if pos == end:
            if shortest_path is None or steps < shortest_path:
                shortest_path = steps
            continue
        tr = (steps + 1) % len(cols)
        tc = (steps + 1) % len(rows)

        if pos == start:
            candidates.append(([pos[0], pos[1]], steps + 1))
            vertical_collisions = all(
                (b[0] + b[1] * tc) % len(rows) != pos[0] + 1 for b in cols[pos[1]]
            )
            if pos[0] == -1:
                horizontal_collision = all(
                    (b[0] + b[1] * tr) % len(cols) != pos[1] for b in rows[pos[0] + 1]
                )
                if horizontal_collision and vertical_collisions:
                    candidates.append(([pos[0] + 1, pos[1]], steps + 1))
            else:
                horizontal_collision = all(
                    (b[0] + b[1] * tr) % len(cols) != pos[1] for b in rows[pos[0] - 1]
                )
                if horizontal_collision and vertical_collisions:
                    candidates.append(([pos[0] - 1, pos[1]], steps + 1))
            continue

        horizontal_collisions = [
            all((b[0] + b[1] * tr) % len(cols) != pos[1] - 1 for b in rows[pos[0]])
            if 0 <= pos[1] - 1 < len(cols)
            else False,
            all((b[0] + b[1] * tr) % len(cols) != pos[1] for b in rows[pos[0] - 1])
            if 0 <= pos[0] - 1 < len(rows)
            else False,
            all((b[0] + b[1] * tr) % len(cols) != pos[1] for b in rows[pos[0]]),
            all((b[0] + b[1] * tr) % len(cols) != pos[1] for b in rows[pos[0] + 1])
            if 0 <= pos[0] + 1 < len(rows)
            else False,
            all((b[0] + b[1] * tr) % len(cols) != pos[1] + 1 for b in rows[pos[0]])
            if 0 <= pos[1] + 1 < len(cols)
            else False,
        ]

        vertical_collisions = [
            all((b[0] + b[1] * tc) % len(rows) != pos[0] for b in cols[pos[1] - 1])
            if 0 <= pos[1] - 1 < len(cols)
            else False,
            all((b[0] + b[1] * tc) % len(rows) != pos[0] - 1 for b in cols[pos[1]])
            if 0 <= pos[0] - 1 < len(rows)
            else False,
            all((b[0] + b[1] * tc) % len(rows) != pos[0] for b in cols[pos[1]]),
            all((b[0] + b[1] * tc) % len(rows) != pos[0] + 1 for b in cols[pos[1]])
            if 0 <= pos[0] + 1 < len(rows)
            else False,
            all((b[0] + b[1] * tc) % len(rows) != pos[0] for b in cols[pos[1] + 1])
            if 0 <= pos[1] + 1 < len(cols)
            else False,
        ]
        possible_moves = []
        # left
        if vertical_collisions[0] and horizontal_collisions[0]:
            possible_moves.append([pos[0], pos[1] - 1])
        # up
        if horizontal_collisions[1] and vertical_collisions[1]:
            possible_moves.append([pos[0] - 1, pos[1]])
        # still
        if horizontal_collisions[2] and vertical_collisions[2]:
            possible_moves.append(pos)
        # down
        if horizontal_collisions[3] and vertical_collisions[3]:
            possible_moves.append([pos[0] + 1, pos[1]])
        # right
        if vertical_collisions[4] and horizontal_collisions[4]:
            possible_moves.append([pos[0], pos[1] + 1])

        # prioritize moves that are closer to the end
        if start[0] > end[0]:
            possible_moves = possible_moves[::-1]

        for new_pos in possible_moves:
            if new_pos not in visited.get(steps + 1, []):
                visited[steps + 1] = visited.get(steps + 1, []) + [new_pos]
                candidates.append((new_pos, steps + 1))

    return shortest_path + 1


def part_a(data):
    rows, cols = parse_data(data)
    start = [-1, 0]
    end = [len(rows) - 1, len(cols) - 1]
    return find_path(rows, cols, start, end)


def part_b(data):
    rows, cols = parse_data(data)
    steps_go = find_path(rows, cols, [-1, 0], [len(rows) - 1, len(cols) - 1])
    steps_return = find_path(rows, cols, [len(rows), len(cols) - 1], [0, 0], steps_go)
    steps_go_again = find_path(
        rows, cols, [-1, 0], [len(rows) - 1, len(cols) - 1], steps_return
    )
    return steps_go_again


aoc_data = get_data(day=DAY, year=YEAR).splitlines()
test_data = """\
#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#""".splitlines()

if __name__ == "__main__":
    assert part_a(test_data) == 18
    assert part_b(test_data) == 54
    print(part_a(aoc_data))
    print(part_b(aoc_data))
