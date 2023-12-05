from aocd import get_data

DAY, YEAR = 4, 2023


def parse_data(data):
    cards = []
    for line in data:
        card, lists = line.split(": ")
        cards.append((set(map(int, l.split())) for l in lists.split(" | ")))
    return cards


def part_a(data):
    cards = parse_data(data)

    s = 0
    for (win, nums) in cards:
        winning_cards = win.intersection(nums)
        s += 2 ** (len(winning_cards) - 1) if winning_cards else 0
    return s


def part_b(data):
    cards = parse_data(data)

    copies = {}
    for idx, (win, nums) in enumerate(cards):
        copies[idx] = copies.get(idx, 0) + 1
        winning_cards = len(win.intersection(nums))
        for i in range(idx + 1, winning_cards + idx + 1):
            copies[i] = copies.get(i, 0) + copies[idx]

    return sum(copies.values())


aoc_data = get_data(day=DAY, year=YEAR).splitlines()
test_data = """\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
""".splitlines()

if __name__ == "__main__":
    assert part_a(test_data) == 13
    assert part_b(test_data) == 30
    print(part_a(aoc_data))
    print(part_b(aoc_data))
