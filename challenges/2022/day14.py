from aocd import get_data

DAY, YEAR = 14, 2022


def create_grid(data):
    grid = {}
    max_y = 0
    for line in data:
        coord_list = [
            [int(c.split(",")[0]), int(c.split(",")[1])] for c in line.split(" -> ")
        ]
        for i in range(len(coord_list) - 1):
            x0, y0 = coord_list[i]
            x1, y1 = coord_list[i + 1]
            if x0 == x1:
                for y in range(min(y0, y1), max(y0, y1) + 1):
                    grid[(x0, y)] = 1
            else:
                for x in range(min(x0, x1), max(x0, x1) + 1):
                    grid[(x, y0)] = 1
            max_y = max(max_y, y0, y1)
    return grid, max_y


def find_spot(grid, x, y, max_y, floor=False):
    if (not floor) and y > max_y:
        return -1, -1
    if floor and y >= max_y + 1:
        return x, y

    if grid.get((x, y + 1), 0) == 0:
        return find_spot(grid, x, y + 1, max_y, floor)
    if grid.get((x - 1, y + 1), 0) == 0:
        return find_spot(grid, x - 1, y + 1, max_y, floor)
    if grid.get((x + 1, y + 1), 0) == 0:
        return find_spot(grid, x + 1, y + 1, max_y, floor)
    return x, y


def part_a(data):
    grid, max_y = create_grid(data)
    x0, y0 = 500, 0
    count = 0
    while True:
        x, y = find_spot(grid, x0, y0, max_y)
        if x == -1:
            break
        grid[(x, y)] = 2
        count += 1
    return count


def part_b(data):
    grid, max_y = create_grid(data)
    x0, y0 = 500, 0
    count = 0
    while True:
        x, y = find_spot(grid, x0, y0, max_y, floor=True)
        if x == x0 and y == y0:
            count += 1
            break
        grid[(x, y)] = 2
        count += 1
    return count


aoc_data = get_data(day=DAY, year=YEAR).splitlines()
test_data = """\
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""".splitlines()

if __name__ == "__main__":
    assert part_a(test_data) == 24
    assert part_b(test_data) == 93
    print(part_a(aoc_data))
    print(part_b(aoc_data))
