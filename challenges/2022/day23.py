from aocd import get_data

DAY, YEAR = 23, 2022

MOVE_ORDER = [
    [(-1, i) for i in range(-1, 2)],
    [(1, i) for i in range(-1, 2)],
    [(i, -1) for i in range(-1, 2)],
    [(i, 1) for i in range(-1, 2)],
]

DIRECTION_ORDER = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def parse_data(data):
    elves = {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "#":
                elves[(i, j)] = 1
    return elves


def play_round(round_num, elves):
    proposals = {}
    for elf in elves:
        possible_moves = [True] * 4
        for i in range(4):
            j = (round_num + i) % 4
            for dr, dc in MOVE_ORDER[j]:
                possible_moves[j] = (
                    possible_moves[j] and (elf[0] + dr, elf[1] + dc) not in elves
                )
        if all(possible_moves) or not any(possible_moves):
            new_position = elf
        else:
            direction_idx = min(
                (i - round_num) % 4 for i in range(4) if possible_moves[i]
            )
            dr, dc = DIRECTION_ORDER[(round_num + direction_idx) % 4]
            new_position = (elf[0] + dr, elf[1] + dc)
        proposals[new_position] = proposals.get(new_position, []) + [elf]

    new_elves = {}
    for elf, proposal_list in proposals.items():
        if len(proposal_list) == 1:
            new_elves[elf] = 1
        else:
            for pelf in proposal_list:
                new_elves[pelf] = 1

    return new_elves


def part_a(data):
    elves = parse_data(data)
    for r in range(10):
        elves = play_round(r, elves)
    mr = min(elves.keys(), key=lambda x: x[0])[0]
    mc = min(elves.keys(), key=lambda x: x[1])[1]
    Mr = max(elves.keys(), key=lambda x: x[0])[0]
    Mc = max(elves.keys(), key=lambda x: x[1])[1]
    return (Mr - mr + 1) * (Mc - mc + 1) - len(elves)


def part_b(data):
    elves = parse_data(data)
    finished = False
    r = 0
    while not finished:
        nelves = play_round(r, elves)
        finished = nelves == elves
        elves = nelves
        r += 1
    return r


aoc_data = get_data(day=DAY, year=YEAR).splitlines()
test_data = """\
....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..""".splitlines()

if __name__ == "__main__":
    assert part_a(test_data) == 110
    assert part_b(test_data) == 20
    print(part_a(aoc_data))
    print(part_b(aoc_data))
