from aocd import get_data

DAY, YEAR = 12, 2022


def convert_to_graph(data):
    graph = {}
    start = end = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "S":
                start = (i, j)
                letter = "a"
            elif data[i][j] == "E":
                end = (i, j)
                letter = "z"
            else:
                letter = data[i][j]
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < len(data) and 0 <= y < len(data[i]):
                    xy_letter = data[x][y]
                    if xy_letter == "S":
                        xy_letter = "a"
                    elif xy_letter == "E":
                        xy_letter = "z"
                    if ord(letter) + 1 >= ord(xy_letter):
                        graph.setdefault((i, j), []).append((x, y))

    return graph, start, end


def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]


def a_star(graph, start, end):
    open_set = {start}
    came_from = {}
    g_score = {start: 0}
    f_score = {start: 0}

    while open_set:
        current = min(open_set, key=lambda x: f_score[x])
        if current == end:
            return reconstruct_path(came_from, current)

        open_set.remove(current)
        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = (
                    tentative_g_score
                    + abs(end[0] - neighbor[0])
                    + abs(end[1] - neighbor[1])
                )
                open_set.add(neighbor)
    return None


def part_a(data):
    graph, start, end = convert_to_graph(data)
    path = a_star(graph, start, end)
    return len(path) - 1


def part_b(data):
    graph, start, end = convert_to_graph(data)
    possible_starts = [start] + [
        (i, j)
        for i in range(len(data))
        for j in range(len(data[i]))
        if data[i][j] == "a"
    ]
    steps = []
    for start in possible_starts:
        path = a_star(graph, start, end)
        if path:
            steps.append(len(path) - 1)
    return min(steps)


aoc_data = get_data(day=DAY, year=YEAR).splitlines()
test_data = """\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".splitlines()

if __name__ == "__main__":
    assert part_a(test_data) == 31
    assert part_b(test_data) == 29
    print(part_a(aoc_data))
    print(part_b(aoc_data))
