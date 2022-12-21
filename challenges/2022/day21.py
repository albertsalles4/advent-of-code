from aocd import get_data

DAY, YEAR = 21, 2022


def parse_data(data):
    monkeys = {}
    for line in data:
        s1, s2 = line.split(": ")
        if s2.isdigit():
            monkeys[s1] = int(s2)
        else:
            monkeys[s1] = list(s2.split())
    return monkeys


def construct(monkeys, current_monkey):
    if not isinstance(monkeys[current_monkey], list):
        return monkeys[current_monkey]
    m1, op, m2 = monkeys[current_monkey]
    m1 = construct(monkeys, m1)
    m2 = construct(monkeys, m2)
    if isinstance(m1, int) and isinstance(m2, int):
        return int(eval(f"{m1} {op} {m2}"))
    return tuple((m1, op, m2))


def part_a(data):
    monkeys = parse_data(data)
    return construct(monkeys, "root")


def solve_for_X(eqX, eqY):
    if eqX == "X":
        return eqY
    left, op, right = eqX
    if op == "+":
        if isinstance(right, int):
            return solve_for_X(left, eqY - right)
        return solve_for_X(right, eqY - left)
    if op == "-":
        if isinstance(right, int):
            return solve_for_X(left, eqY + right)
        return solve_for_X(right, left - eqY)
    if op == "*":
        if isinstance(right, int):
            return solve_for_X(left, eqY // right)
        return solve_for_X(right, eqY // left)
    if op == "/":
        if isinstance(right, int):
            return solve_for_X(left, eqY * right)
        return solve_for_X(right, left // eqY)
    return -1


def part_b(data):
    monkeys = parse_data(data)
    monkeys["root"][1] = "="
    monkeys["humn"] = "X"
    equation = construct(monkeys, "root")
    return solve_for_X(equation[0], equation[2])


aoc_data = get_data(day=DAY, year=YEAR).splitlines()
test_data = """\
root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32""".splitlines()

if __name__ == "__main__":
    assert part_a(test_data) == 152
    assert part_b(test_data) == 301
    print(part_a(aoc_data))
    print(part_b(aoc_data))
