from aocd import get_data

DAY, YEAR = 11, 2022


def parse_input(data):
    monkeys = [{} for _ in range((len(data) + 1) // 7)]
    for m in range(1, len(data), 7):
        monkeys[m // 7]["items"] = [int(i) for i in data[m][18:].split(", ")]
        monkeys[m // 7]["op"] = data[m + 1][19:]
        monkeys[m // 7]["test"] = int(data[m + 2].split()[-1])
        monkeys[m // 7]["True"] = int(data[m + 3].split()[-1])
        monkeys[m // 7]["False"] = int(data[m + 4].split()[-1])
        monkeys[m // 7]["inspects"] = 0
    return monkeys


def get_business_level(monkeys, rounds, divider):
    mcm = 1
    for m in monkeys:
        mcm *= m["test"]
    for r in range(rounds):
        for m in monkeys:
            for old in m["items"]:
                m["inspects"] += 1
                new = eval(m["op"]) // divider
                monkeys[m[str(new % m["test"] == 0)]]["items"].append(new % mcm)
            m["items"] = []

    monkeys.sort(key=lambda m: -m["inspects"])
    return monkeys[0]["inspects"] * monkeys[1]["inspects"]


def part_a(data):
    monkeys = parse_input(data)
    return get_business_level(monkeys, 20, 3)


def part_b(data):
    monkeys = parse_input(data)
    return get_business_level(monkeys, 10000, 1)


aoc_data = get_data(day=DAY, year=YEAR).splitlines()
test_data = """\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""".splitlines()

if __name__ == "__main__":
    assert part_a(test_data) == 10605
    assert part_b(test_data) == 2713310158
    print(part_a(aoc_data))
    print(part_b(aoc_data))
