from aocd import get_data

DAY, YEAR = 25, 2022

DIGITS = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}


def SNAFU_to_decimal(s):
    n = 0
    for i, d in enumerate(reversed(s)):
        n += DIGITS[d] * 5**i
    return n


def decimal_to_SNAFU(n):
    reversed_digits = {v % 5: k for k, v in DIGITS.items()}
    s = ""
    c = 0
    while n > 0:
        r = n % 5 + c
        s += reversed_digits[r % 5]
        n //= 5
        c = 1 if r > 2 else 0
    return "1" + s[::-1] if c else s[::-1]


def part_a(data):
    return decimal_to_SNAFU(sum(SNAFU_to_decimal(s) for s in data))


aoc_data = get_data(day=DAY, year=YEAR).splitlines()
test_data = """\
1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122""".splitlines()

if __name__ == "__main__":
    assert part_a(test_data) == "2=-1=0"
    print(part_a(aoc_data))
