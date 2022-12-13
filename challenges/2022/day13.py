from aocd import get_data

DAY, YEAR = 13, 2022


def get_pairs(data):
    return [[eval(data[i]), eval(data[i + 1])] for i in range(0, len(data), 3)]


def right_order(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left < right if left != right else None
    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]

    for i in range(max(len(left), len(right))):
        if i >= len(left):
            return True
        if i >= len(right):
            return False
        response = right_order(left[i], right[i])
        if response is not None:
            return response
    return None


def part_a(data):
    pairs = get_pairs(data)
    return sum(
        [i + 1 for i in range(len(pairs)) if right_order(pairs[i][0], pairs[i][1])]
    )


def merge(data1, data2, greater):
    result = []
    while len(data1) > 0 and len(data2) > 0:
        if greater(data1[0], data2[0]):
            result.append(data1.pop(0))
        else:
            result.append(data2.pop(0))
    result += data1
    result += data2
    return result


def mergesort(data, greater):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = mergesort(data[:mid], greater)
    right = mergesort(data[mid:], greater)
    return merge(left, right, greater)


def part_b(data):
    p1, p2 = [[2]], [[6]]
    lines = [p1, p2] + [eval(line) for line in data if line]
    lines = mergesort(lines, right_order)
    return (lines.index(p1) + 1) * (lines.index(p2) + 1)


aoc_data = get_data(day=DAY, year=YEAR).splitlines()
test_data = """\
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]""".splitlines()

if __name__ == "__main__":
    assert part_a(test_data) == 13
    assert part_b(test_data) == 140
    print(part_a(aoc_data))
    print(part_b(aoc_data))
