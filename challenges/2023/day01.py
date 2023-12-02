from aocd import get_data

DAY, YEAR = 1, 2023


def part_a(data):
    s = 0
    for line in data:
        i = 0
        ni, nj = None, None
        while ni is None or nj is None:
            if ni is None and line[i].isdigit():
                ni = line[i]
            if nj is None and line[len(line) - i - 1].isdigit():
                nj = line[len(line) - i - 1]

            i += 1

        s += int(ni + nj)
    return s


def part_b(data):
    nums = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    for i in range(1, 10):
        nums[str(i)] = i

    s = 0

    for line in data:
        i = 0
        ni, nj = None, None
        while ni is None or nj is None:
            for k in range(1, 6):
                if ni is None and line[i:i + k] in nums:
                    ni = nums[line[i:i + k]]
                if nj is None and line[len(line) - i - k:len(line) - i] in nums:
                    nj = nums[line[len(line) - i - k:len(line) - i]]
            i += 1

        s += ni * 10 + nj
    return s


aoc_data = get_data(day=DAY, year=YEAR).splitlines()
test_data = """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""".splitlines()
test_data2 = """\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
""".splitlines()

if __name__ == "__main__":
    assert part_a(test_data) == 142
    assert part_b(test_data2) == 281
    print(part_a(aoc_data))
    print(part_b(aoc_data))
