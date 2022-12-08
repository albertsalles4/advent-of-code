from aocd import get_data

DAY, YEAR = 8, 2022


def part_a(data):
    visible = [[0 for _ in range(len(data[j]))] for j in range(len(data))]
    for i in range(len(data)):
        m = -1
        for j in range(len(data[i])):
            h_tree = int(data[i][j])
            if h_tree > m:
                m = h_tree
                visible[i][j] = 1
            if m == 9:
                break
        m = -1
        for j in range(len(data[i]) - 1, -1, -1):
            h_tree = int(data[i][j])
            if h_tree > m:
                m = h_tree
                visible[i][j] = 1
            if m == 9:
                break
    for j in range(len(data[0])):
        m = -1
        for i in range(len(data)):
            h_tree = int(data[i][j])
            if h_tree > m:
                m = h_tree
                visible[i][j] = 1
            if m == 9:
                break
        m = -1
        for i in range(len(data) - 1, -1, -1):
            h_tree = int(data[i][j])
            if h_tree > m:
                m = h_tree
                visible[i][j] = 1
            if m == 9:
                break
    return sum([sum(x) for x in visible])


def find_visible_trees(data, i, j):
    h_tree = int(data[i][j])
    trees = [-1, -1, -1, -1]
    # left
    c = 0
    for k in range(j - 1, -1, -1):
        if int(data[i][k]) < h_tree:
            c += 1
        else:
            c += 1
            break
    trees[0] = c
    # up
    c = 0
    for k in range(i - 1, -1, -1):
        if int(data[k][j]) < h_tree:
            c += 1
        else:
            c += 1
            break
    trees[1] = c
    # right
    c = 0
    for k in range(j + 1, len(data[i])):
        if int(data[i][k]) < h_tree:
            c += 1
        else:
            c += 1
            break
    trees[2] = c
    # down
    c = 0
    for k in range(i + 1, len(data)):
        if int(data[k][j]) < h_tree:
            c += 1
        else:
            c += 1
            break
    trees[3] = c
    return trees


def part_b(data):
    trees = [[[-1, -1, -1, -1] for _ in range(len(data[j]))] for j in range(len(data))]
    for i in range(len(data)):
        for j in range(len(data[i])):
            trees[i][j] = find_visible_trees(data, i, j)

    return max([max([x[0] * x[1] * x[2] * x[3] for x in line]) for line in trees])


aoc_data = get_data(day=DAY, year=YEAR).splitlines()
test_data = """\
30373
25512
65332
33549
35390""".splitlines()

if __name__ == "__main__":
    assert part_a(test_data) == 21
    assert part_b(test_data) == 8
    print(part_a(aoc_data))
    print(part_b(aoc_data))
