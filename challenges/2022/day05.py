from aocd import get_data

DAY, YEAR = 5, 2022


def read_input(data):
    num_cols = (len(data[0]) + 1) // 4
    empty_line = False
    i = 0
    while not empty_line:
        i += 1
        empty_line = data[i] == ""
    stacks = [
        [data[j][1 + 4 * k] for j in range(i - 2, -1, -1) if data[j][1 + 4 * k] != " "]
        for k in range(num_cols)
    ]
    instructions = [
        [int(s) for s in line.split() if s.isdigit()] for line in data[i + 1 :]
    ]
    return stacks, instructions


def part_a(data):
    stacks, instructions = read_input(data)

    for n, s0, s1 in instructions:
        for _ in range(n):
            stacks[s1 - 1].append(stacks[s0 - 1].pop())

    result = ""
    for s in stacks:
        if s:
            result += s.pop()
    return result


def part_b(data):
    stacks, instructions = read_input(data)

    for n, s0, s1 in instructions:
        stacks[s1 - 1] += stacks[s0 - 1][-n:]
        stacks[s0 - 1] = stacks[s0 - 1][:-n]

    result = ""
    for s in stacks:
        if s:
            result += s.pop()
    return result


aoc_data = get_data(day=DAY, year=YEAR).split("\n")
test_data = """\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""".split(
    "\n"
)

if __name__ == "__main__":
    assert part_a(test_data) == "CMZ"
    assert part_b(test_data) == "MCD"
    print(part_a(aoc_data))
    print(part_b(aoc_data))
