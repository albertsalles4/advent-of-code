from aocd import get_data

DAY, YEAR = 5, 2023


def parse(data):
    d = {"seeds": [int(x) for x in data[0].split(": ")[1].split()], "maps": []}

    latest_map = ""
    for line in data[2:]:
        if line == "":
            continue
        if not line[0].isdigit():
            latest_map = line.split()[0]
            d["maps"].append(latest_map)
            d[latest_map] = []
            continue
        d[latest_map].append([int(x) for x in line.split()])

    return d


def part_a(data):
    maps = parse(data)

    location = None
    for seed in maps["seeds"]:
        seed_loc = seed
        for m in maps["maps"]:
            for row in maps[m]:
                if row[1] <= seed_loc <= row[1] + row[2]:
                    seed_loc = row[0] + (seed_loc - row[1])
                    break
        location = seed_loc if location is None else min(location, seed_loc)

    return location


def part_b(data):
    maps = parse(data)
    maps["seed_pairs"] = [(maps["seeds"][i], maps["seeds"][i] + maps["seeds"][i + 1]) for i in
                          range(0, len(maps["seeds"]), 2)]

    seed_loc = maps["seed_pairs"]
    for m in maps["maps"]:
        new_seed_loc = []
        for p in seed_loc:
            latest_seed_loc = [p]
            while latest_seed_loc:
                x0, x1 = latest_seed_loc.pop()
                found_transformation = False
                for row in maps[m]:
                    dest, source, ran = row
                    new_x0, new_x1 = None, None
                    if source <= x0 <= source + ran:
                        l = x0
                        new_x0 = dest + (x0 - source)
                    elif x0 <= source <= x1:
                        l = source
                        new_x0 = dest
                    if source <= x1 <= source + ran:
                        r = x1
                        new_x1 = dest + (x1 - source)
                    elif x0 <= source + ran <= x1:
                        r = source + ran
                        new_x1 = dest + ran

                    if new_x0 is not None and new_x1 is not None:
                        found_transformation = True
                        new_seed_loc.append((new_x0, new_x1))
                        if l != x0:
                            latest_seed_loc.append((x0, l - 1))
                        if r != x1:
                            latest_seed_loc.append((r + 1, x1))
                if not found_transformation:
                    new_seed_loc.append((x0, x1))

        seed_loc = new_seed_loc

    return min(map(min, seed_loc))


aoc_data = get_data(day=DAY, year=YEAR).splitlines()
test_data = """\
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""".splitlines()

if __name__ == "__main__":
    assert part_a(test_data) == 35
    assert part_b(test_data) == 46
    print(part_a(aoc_data))
    print(part_b(aoc_data))
