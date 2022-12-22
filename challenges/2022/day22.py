from aocd import get_data

DAY, YEAR = 22, 2022

DIRECTION = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}
ROTATION = [">", "v", "<", "^"]


def parse_data(data):
    grid = [[l for l in line] for line in data[:-2]]
    M = max(len(line) for line in grid)
    grid = [line + [" "] * (M - len(line)) for line in grid]
    rows = []
    cols = []
    for i in range(len(grid)):
        start, end = None, None
        for j in range(len(grid[i])):
            if start is None and grid[i][j] != " ":
                start = j
            if start is not None and grid[i][j] == " ":
                end = j - 1
                break
        if end is None:
            end = len(grid[i]) - 1
        rows.append((start, end))

    for j in range(len(grid[0])):
        start, end = None, None
        for i in range(len(grid)):
            if start is None and grid[i][j] != " ":
                start = i
            if start is not None and grid[i][j] == " ":
                end = i - 1
                break
        if end is None:
            end = len(grid) - 1
        cols.append((start, end))

    instructions = [data[-1][0]]
    for i in range(1, len(data[-1])):
        l = data[-1][i]
        b4 = data[-1][i - 1]
        if l.isdigit() and b4.isdigit():
            instructions[-1] += l
        else:
            instructions.append(l)

    instructions = [int(i) if i.isdigit() else i for i in instructions]

    return grid, rows, cols, instructions


def follow_instructions(grid, rows, cols, instructions, compute_next):
    face = ">"
    row, col = 0, rows[0][0]
    for i in instructions:
        if i == "L":
            face = ROTATION[(ROTATION.index(face) - 1) % 4]
            continue
        if i == "R":
            face = ROTATION[(ROTATION.index(face) + 1) % 4]
            continue
        for _ in range(i):
            grid[row][col] = face
            next_row, next_col, face = compute_next((row, col), face, rows, cols)
            if grid[next_row][next_col] == "#":
                face = grid[row][col]
                break
            row, col = next_row, next_col
    return 1000 * (row + 1) + 4 * (col + 1) + ROTATION.index(face)


def compute_next_parta(pos, face, rows, cols):
    row, col = pos
    dr, dc = DIRECTION[face]
    next_row, next_col = row + dr, col + dc
    if next_row < cols[col][0]:
        next_row = cols[col][1]
    if next_row > cols[col][1]:
        next_row = cols[col][0]
    if next_col < rows[row][0]:
        next_col = rows[row][1]
    if next_col > rows[row][1]:
        next_col = rows[row][0]
    return next_row, next_col, face


def part_a(data):
    grid, rows, cols, instructions = parse_data(data)
    return follow_instructions(grid, rows, cols, instructions, compute_next_parta)


def compute_next_partb_HARDCODED_example(pos, face, rows, cols, face_size=4):
    row, col = pos
    dr, dc = DIRECTION[face]
    if (
        cols[col][0] <= row + dr <= cols[col][1]
        and rows[row][0] <= col + dc <= rows[row][1]
    ):
        return row + dr, col + dc, face
    if face == ">":
        if row < face_size or 2 * face_size <= row:
            next_row = 3 * face_size - row - 1
            next_col = rows[next_row][1]
            face = "<"
        else:
            next_col = 4 * face_size - (row - face_size) - 1
            next_row = cols[next_col][0]
            face = "v"
    elif face == "v":
        if col < face_size or 2 * face_size <= col < 3 * face_size:
            next_col = 3 * face_size - col - 1
            next_row = cols[next_col][1]
            face = "^"
        elif face_size <= col < 2 * face_size:
            next_row = 3 * face_size - (col - face_size) - 1
            next_col = rows[next_row][0]
            face = ">"
        else:
            next_row = 4 * face_size - (col - face_size) - 1
            next_col = rows[next_row][0]
            face = ">"
    elif face == "<":
        if row < face_size:
            next_col = row + face_size
            next_row = cols[next_col][0]
            face = "v"
        elif 2 * face_size <= row:
            next_col = 4 * face_size - (row - face_size) - 1
            next_row = cols[next_col][1]
            face = "^"
        else:
            next_col = 3 * face_size - (row - face_size) - 1
            next_row = cols[next_col][1]
            face = "^"
    else:
        if col < face_size or 2 * face_size <= col < 3 * face_size:
            next_col = 3 * face_size - col - 1
            next_row = cols[next_col][0]
            face = "v"
        elif face_size <= col < 2 * face_size:
            next_row = col - face_size
            next_col = rows[next_row][0]
            face = ">"
        else:
            next_row = 4 * face_size - (col - face_size) - 1
            next_col = rows[next_row][1]
            face = "<"
    return next_row, next_col, face


def compute_next_partb_HARDCODED_big(pos, face, rows, cols, face_size=50):
    row, col = pos
    dr, dc = DIRECTION[face]
    if (
        cols[col][0] <= row + dr <= cols[col][1]
        and rows[row][0] <= col + dc <= rows[row][1]
    ):
        return row + dr, col + dc, face
    if face == ">":
        if row < face_size or 2 * face_size <= row < 3 * face_size:
            next_row = 3 * face_size - row - 1
            next_col = rows[next_row][1]
            face = "<"
        elif face_size <= row < 2 * face_size:
            next_col = row + face_size
            next_row = cols[next_col][1]
            face = "^"
        else:
            next_col = row - 2 * face_size
            next_row = cols[next_col][1]
            face = "^"
    elif face == "v":
        if col < face_size:
            next_col = col + 2 * face_size
            next_row = cols[next_col][0]
            face = "v"
        elif face_size <= col < 2 * face_size:
            next_row = col + 2 * face_size
            next_col = rows[next_row][1]
            face = "<"
        else:
            next_row = col - face_size
            next_col = rows[next_row][1]
            face = "<"
    elif face == "<":
        if row < face_size or 2 * face_size <= row < 3 * face_size:
            next_row = 3 * face_size - row - 1
            next_col = rows[next_row][0]
            face = ">"
        elif face_size <= row < 2 * face_size:
            next_col = row - face_size
            next_row = cols[next_col][0]
            face = "v"
        else:
            next_col = row - 2 * face_size
            next_row = cols[next_col][0]
            face = "v"
    else:
        if col < face_size:
            next_row = col + face_size
            next_col = rows[next_row][0]
            face = ">"
        elif face_size <= col < 2 * face_size:
            next_row = col + 2 * face_size
            next_col = rows[next_row][0]
            face = ">"
        else:
            next_col = col - 2 * face_size
            next_row = cols[next_col][1]
            face = "^"
    return next_row, next_col, face


def part_b(data, test=False):
    grid, rows, cols, instructions = parse_data(data)
    compute_next = (
        compute_next_partb_HARDCODED_big
        if not test
        else compute_next_partb_HARDCODED_example
    )
    return follow_instructions(grid, rows, cols, instructions, compute_next)


aoc_data = get_data(day=DAY, year=YEAR).splitlines()
test_data = """\
        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5""".splitlines()

if __name__ == "__main__":
    assert part_a(test_data) == 6032
    assert part_b(test_data, test=True) == 5031
    print(part_a(aoc_data))
    print(part_b(aoc_data))
