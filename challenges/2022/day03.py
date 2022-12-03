from aocd import get_data

DAY, YEAR = 3, 2022


def part_a(data):
    s = 0
    for rucksack in data:
        c1 = sorted(rucksack[: len(rucksack) // 2])
        c2 = sorted(rucksack[len(rucksack) // 2 :])
        letter = ""
        i, j = 0, 0
        while not letter:
            if c1[i] == c2[j]:
                letter = c1[i]
            elif c1[i] < c2[j]:
                i += 1
            else:
                j += 1
        ascii_code = ord(letter)
        # ord('a') := 97 and ord('A') := 65
        s += ascii_code - 96 if ascii_code > 97 else ascii_code - 38
    return s


def part_b(data):
    s = 0
    for group in range(0, len(data), 3):
        r1 = sorted(data[group])
        r2 = sorted(data[group + 1])
        r3 = sorted(data[group + 2])
        letter = ""
        i, j, k = 0, 0, 0
        while not letter:
            if r1[i] == r2[j] == r3[k]:
                letter = r1[i]
                continue
            elif r1[i] <= r2[j] and r1[i] <= r3[k]:
                i += 1
            elif r2[j] <= r1[i] and r2[j] <= r3[k]:
                j += 1
            elif r3[k] <= r2[j] and r3[k] <= r1[i]:
                k += 1
        ascii_code = ord(letter)
        # ord('a') := 97 and ord('A') := 65
        s += ascii_code - 96 if ascii_code > 97 else ascii_code - 38
    return s


aoc_data = get_data(day=DAY, year=YEAR).split("\n")
test_data = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".split(
    "\n"
)

if __name__ == "__main__":
    assert part_a(test_data) == 157
    assert part_b(test_data) == 70
    print(part_a(aoc_data))
    print(part_b(aoc_data))
