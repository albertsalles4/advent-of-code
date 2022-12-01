from aocd import get_data

DAY, YEAR = 0, 0


def part_a(data):
    pass


def part_b(data):
    pass


aoc_data = get_data(day=DAY, year=YEAR).split("\n")
test_data = """\
some example test data
""".split(
    "\n"
)

if __name__ == "__main__":
    assert part_a(test_data) == "expected test result a"
    assert part_b(test_data) == "expected test result b"
    print(part_a(aoc_data))
    print(part_b(aoc_data))
