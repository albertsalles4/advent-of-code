from aocd import get_data

DAY, YEAR = 0, 0


def part_a(data):
    pass


def part_b(data):
    pass


aoc_data = get_data(day=DAY, year=YEAR).splitlines()
test_data = """\
some example test data
""".splitlines()

if __name__ == "__main__":
    assert part_a(test_data) is None
    assert part_b(test_data) is None
    print(part_a(aoc_data))
    print(part_b(aoc_data))
