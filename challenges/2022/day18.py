from aocd import get_data

DAY, YEAR = 18, 2022


def get_cubes(data):
    return [[int(x) for x in line.split(",")] for line in data]


def count_sides(cubes):
    grid = {}
    for cube in cubes:
        sides = 0
        for x, y, z in [
            (1, 0, 0),
            (-1, 0, 0),
            (0, 1, 0),
            (0, -1, 0),
            (0, 0, 1),
            (0, 0, -1),
        ]:
            if (cube[0] + x, cube[1] + y, cube[2] + z) not in grid:
                sides += 1
            else:
                grid[(cube[0] + x, cube[1] + y, cube[2] + z)] -= 1
        grid[tuple(cube)] = sides
    return grid


def part_a(data):
    cubes = get_cubes(data)
    grid = count_sides(cubes)
    return sum(grid.values())


def fill_grid(grid, pos, m, M):
    candidates = [pos]
    while candidates:
        cube = candidates.pop()
        for x, y, z in [
            (1, 0, 0),
            (-1, 0, 0),
            (0, 1, 0),
            (0, -1, 0),
            (0, 0, 1),
            (0, 0, -1),
        ]:
            grid[tuple(cube)] = 0
            if (
                m[0] <= cube[0] + x <= M[0]
                and m[1] <= cube[1] + y <= M[1]
                and m[2] <= cube[2] + z <= M[2]
            ):
                if (cube[0] + x, cube[1] + y, cube[2] + z) not in grid:
                    candidates.append((cube[0] + x, cube[1] + y, cube[2] + z))
    return grid


def fill_interior(grid, pos):
    candidates = [pos]
    while candidates:
        cube = candidates.pop()
        grid[tuple(cube)] = 0
        for x, y, z in [
            (1, 0, 0),
            (-1, 0, 0),
            (0, 1, 0),
            (0, -1, 0),
            (0, 0, 1),
            (0, 0, -1),
        ]:
            if (cube[0] + x, cube[1] + y, cube[2] + z) not in grid:
                candidates.append((cube[0] + x, cube[1] + y, cube[2] + z))
            elif grid[(cube[0] + x, cube[1] + y, cube[2] + z)] > 0:
                grid[tuple(cube)] -= 1
    return grid


def part_b(data):
    cubes = get_cubes(data)
    grid = count_sides(cubes)
    mx, my, mz = cubes[0]
    Mx, My, Mz = cubes[0]
    for cube in cubes:
        mx, my, mz = min(mx, cube[0]), min(my, cube[1]), min(mz, cube[2])
        Mx, My, Mz = max(Mx, cube[0]), max(My, cube[1]), max(Mz, cube[2])

    m = (mx - 1, my - 1, mz - 1)
    M = (Mx + 1, My + 1, Mz + 1)
    pos = m
    grid = fill_grid(grid, pos, m, M)
    for x in range(mx, Mx + 1):
        for y in range(my, My + 1):
            for z in range(mz, Mz + 1):
                if (x, y, z) not in grid:
                    grid = fill_interior(grid, (x, y, z))
    return sum(grid.values())


aoc_data = get_data(day=DAY, year=YEAR).splitlines()
test_data = """\
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5""".splitlines()

if __name__ == "__main__":
    assert part_a(test_data) == 64
    assert part_b(test_data) == 58
    print(part_a(aoc_data))
    print(part_b(aoc_data))
