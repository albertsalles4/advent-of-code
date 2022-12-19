from aocd import get_data

DAY, YEAR = 19, 2022


def parse_data(data):
    blueprints = []
    for line in data:
        or_rcor, cl_rcor, ob_rcor, ob_rccl, ge_rcor, ge_rcob = [
            int(x) for x in line.split() if x.isdigit()
        ]
        blueprints.append(
            {
                "ore_robot": (or_rcor, 0, 0),
                "clay_robot": (cl_rcor, 0, 0),
                "obsidian_robot": (ob_rcor, ob_rccl, 0),
                "geo_robot": (ge_rcor, 0, ge_rcob),
            }
        )
    return blueprints


def heuristic(ge_robot, min_left):
    return ge_robot * min_left + min_left * (min_left + 1) // 2


def get_max_geodes(blueprint, minutes=24):
    ore, clay, obsidian, geodes, min_left = 0, 0, 0, 0, minutes
    max_ore_needed = max(
        blueprint["ore_robot"][0],
        blueprint["clay_robot"][0],
        blueprint["obsidian_robot"][0],
        blueprint["geo_robot"][0],
    )
    max_clay_needed = blueprint["obsidian_robot"][1]
    max_obsidian_needed = blueprint["geo_robot"][2]
    material = (ore, clay, obsidian, geodes)
    robots = (0, 0, 0, 0)
    skip_robots = {"or_robot": False, "cl_robot": False, "ob_robot": False}
    candidates = [(material, robots, min_left, skip_robots)]
    best_geodes = 0
    while candidates:
        material, robots, min_left, skip_robots = candidates.pop(-1)
        ore, clay, obsidian, geodes = material
        or_robot, cl_robot, ob_robot, ge_robot = robots
        if min_left <= 0:
            best_geodes = max(best_geodes, geodes)
            continue
        if geodes + heuristic(ge_robot, min_left) < best_geodes:
            continue

        if (
            ob_robot > 0
            and ore >= blueprint["geo_robot"][0]
            and obsidian >= blueprint["geo_robot"][2]
        ):
            nm = (
                ore - blueprint["geo_robot"][0],
                clay,
                obsidian - blueprint["geo_robot"][2],
                geodes,
            )
            nr = (or_robot, cl_robot, ob_robot, ge_robot + 1)
            nm = (
                nm[0] + 1 + or_robot,
                nm[1] + cl_robot,
                nm[2] + ob_robot,
                nm[3] + ge_robot,
            )
            nsr = {"or_robot": False, "cl_robot": False, "ob_robot": False}
            candidates.append((nm, nr, min_left - 1, nsr))
            continue

        need_obsidian_rob = (
            ob_robot < max_obsidian_needed
            and cl_robot > 0
            and not skip_robots["ob_robot"]
        )
        can_build_obs = (
            ore >= blueprint["obsidian_robot"][0]
            and clay >= blueprint["obsidian_robot"][1]
        )
        if need_obsidian_rob and can_build_obs:
            nm = (
                ore - blueprint["obsidian_robot"][0],
                clay - blueprint["obsidian_robot"][1],
                obsidian,
                geodes,
            )
            nr = (or_robot, cl_robot, ob_robot + 1, ge_robot)
            nm = (
                nm[0] + 1 + or_robot,
                nm[1] + cl_robot,
                nm[2] + ob_robot,
                nm[3] + ge_robot,
            )
            nsr = {"or_robot": False, "cl_robot": False, "ob_robot": False}
            candidates.append((nm, nr, min_left - 1, nsr))
        if can_build_obs:
            skip_robots["ob_robot"] = True

        need_clay_rob = cl_robot < max_clay_needed and not skip_robots["cl_robot"]
        can_build_clay = ore >= blueprint["clay_robot"][0]
        if need_clay_rob and can_build_clay:
            nm = (ore - blueprint["clay_robot"][0], clay, obsidian, geodes)
            nr = (or_robot, cl_robot + 1, ob_robot, ge_robot)
            nm = (
                nm[0] + 1 + or_robot,
                nm[1] + cl_robot,
                nm[2] + ob_robot,
                nm[3] + ge_robot,
            )
            nsr = {"or_robot": False, "cl_robot": False, "ob_robot": False}
            candidates.append((nm, nr, min_left - 1, nsr))
        if can_build_clay:
            skip_robots["cl_robot"] = True

        need_ore_rob = or_robot < max_ore_needed
        can_build_ore = ore >= blueprint["ore_robot"][0]
        if need_ore_rob and can_build_ore:
            nm = (ore - blueprint["ore_robot"][0], clay, obsidian, geodes)
            nr = (or_robot + 1, cl_robot, ob_robot, ge_robot)
            nm = (
                nm[0] + 1 + or_robot,
                nm[1] + cl_robot,
                nm[2] + ob_robot,
                nm[3] + ge_robot,
            )
            nsr = {"or_robot": False, "cl_robot": False, "ob_robot": False}
            candidates.append((nm, nr, min_left - 1, nsr))
        if can_build_ore:
            skip_robots["or_robot"] = True

        if not (can_build_ore and can_build_clay and can_build_obs):
            nm = (
                ore + 1 + or_robot,
                clay + cl_robot,
                obsidian + ob_robot,
                geodes + ge_robot,
            )
            candidates.append((nm, robots, min_left - 1, skip_robots))

    return best_geodes


def part_a(data):
    blueprints = parse_data(data)
    quality_level = 0
    for b, blueprint in enumerate(blueprints):
        geodes = get_max_geodes(blueprint)
        quality_level += (b + 1) * geodes
    return quality_level


def part_b(data):
    blueprints = parse_data(data)[:3]
    quality_level = 1
    for blueprint in blueprints:
        geodes = get_max_geodes(blueprint, minutes=32)
        quality_level *= geodes
    return quality_level


aoc_data = get_data(day=DAY, year=YEAR).splitlines()
test_data = [
    "Blueprint 1: Each ore robot costs 4 ore. "
    "Each clay robot costs 2 ore. "
    "Each obsidian robot costs 3 ore and 14 clay. "
    "Each geode robot costs 2 ore and 7 obsidian.",
    "Blueprint 2: Each ore robot costs 2 ore. "
    "Each clay robot costs 3 ore. "
    "Each obsidian robot costs 3 ore and 8 clay. "
    "Each geode robot costs 3 ore and 12 obsidian.",
]

if __name__ == "__main__":
    assert part_a(test_data) == 33
    assert part_b(test_data) == 56 * 62
    print(part_a(aoc_data))
    print(part_b(aoc_data))
