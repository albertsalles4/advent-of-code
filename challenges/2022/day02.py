from aocd import get_data

DAY, YEAR = 2, 2022


def part_a(data):
    convert = {"A": "X", "B": "Y", "C": "Z"}
    win = {"X": "Z", "Y": "X", "Z": "Y"}
    points = {"X": 1, "Y": 2, "Z": 3}
    score = 0
    for line in data:
        op, me = convert[line[0]], line[-1]
        if me == op:
            score += 3
        elif win[me] == op:
            score += 6
        score += points[me]
    return score


def part_b(data):
    win = {"C": "A", "A": "B", "B": "C"}
    lose = {win[k]: k for k in win}
    points = {"A": 1, "B": 2, "C": 3}
    score = 0
    for line in data:
        op, finish = line[0], line[-1]
        if finish == "X":
            score += points[lose[op]]
        elif finish == "Y":
            score += 3 + points[op]
        else:
            score += 6 + points[win[op]]
    return score


aoc_data = get_data(day=DAY, year=YEAR).split("\n")
test_data = """\
A Y
B X
C Z""".split(
    "\n"
)

if __name__ == "__main__":
    assert part_a(test_data) == 15
    assert part_b(test_data) == 12
    print(part_a(aoc_data))
    print(part_b(aoc_data))
