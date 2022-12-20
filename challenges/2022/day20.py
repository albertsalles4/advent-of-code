from aocd import get_data

DAY, YEAR = 20, 2022


class LinkedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


def mix(nums, start_ln):
    for ln in nums:
        pos = ln.value % (len(nums) - 1)
        ln_prev, ln_next = ln.prev, ln.next
        if pos > 0:
            ln_prev.next, ln_next.prev = ln_next, ln_prev
            for _ in range(pos):
                ln_next = ln_next.next
            ln_next_prev = ln_next.prev
            ln_next_prev.next, ln.prev = ln, ln_next_prev
            ln.next, ln_next.prev = ln_next, ln

    return start_ln


def part_a(data):
    nums = [LinkedNode(int(x)) for x in data]
    start_ln = None
    for i, ln in enumerate(nums):
        ln.next = nums[(i + 1) % len(nums)]
        ln.prev = nums[(i - 1) % len(nums)]
        if ln.value == 0:
            start_ln = ln
    start_ln = mix(nums, start_ln)

    idx = sorted([1000 % len(nums), 2000 % len(nums), 3000 % len(nums)])
    pos, result = 0, 0
    for i in idx:
        while pos < i:
            start_ln = start_ln.next
            pos += 1
        result += start_ln.value
    return result


def part_b(data):
    key = 811589153
    n = 10
    nums = [LinkedNode(int(x) * key) for x in data]
    start_ln = None
    for i, ln in enumerate(nums):
        ln.next = nums[(i + 1) % len(nums)]
        ln.prev = nums[(i - 1) % len(nums)]
        if ln.value == 0:
            start_ln = ln
    for _ in range(n):
        start_ln = mix(nums, start_ln)

    idx = sorted([1000 % len(nums), 2000 % len(nums), 3000 % len(nums)])
    pos, result = 0, 0
    for i in idx:
        while pos < i:
            start_ln = start_ln.next
            pos += 1
        result += start_ln.value
    return result


aoc_data = get_data(day=DAY, year=YEAR).splitlines()
test_data = """\
1
2
-3
3
-2
0
4""".splitlines()

if __name__ == "__main__":
    assert part_a(test_data) == 3
    assert part_b(test_data) == 1623178306
    print(part_a(aoc_data))
    print(part_b(aoc_data))
