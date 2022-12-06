from aocd import get_data

DAY, YEAR = 6, 2022


def part_a(data):
    for i in range(3, len(data)):
        unique_values = set(data[i - 3 : i + 1])
        if len(unique_values) == 4:
            return i + 1


def part_b(data):
    for i in range(13, len(data)):
        unique_values = set(data[i - 13 : i + 1])
        if len(unique_values) == 14:
            return i + 1


aoc_data = get_data(day=DAY, year=YEAR)
test_data = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""

if __name__ == "__main__":
    assert part_a(test_data) == 7
    assert part_b(test_data) == 19
    print(part_a(aoc_data))
    print(part_b(aoc_data))
