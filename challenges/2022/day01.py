from aocd import get_data

DAY, YEAR = 1, 2022


def part_a(data):
    most_calories = 0
    current_elf = 0
    for line in data:
        if line == "":
            most_calories = (
                current_elf if current_elf > most_calories else most_calories
            )
            current_elf = 0
            continue
        current_elf += int(line)
    return most_calories


def part_b(data):
    top_three = []
    current_elf = 0
    for line in data:
        if line == "":
            if len(top_three) < 3:
                top_three.append(current_elf)
            else:
                for elf in top_three:
                    if current_elf > elf:
                        top_three = sorted(top_three + [current_elf])[-3:]
                        break
            current_elf = 0
            continue
        current_elf += int(line)
    return sum(top_three)


aoc_data = get_data(day=DAY, year=YEAR).split("\n")
test_data = """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
""".split(
    "\n"
)

if __name__ == "__main__":
    assert part_a(test_data) == 24000
    assert part_b(test_data) == 45000
    print(part_a(aoc_data))
    print(part_b(aoc_data))
