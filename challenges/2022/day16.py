from aocd import get_data

DAY, YEAR = 16, 2022


def parse_data(data):
    next_nodes = {}
    rates = {}
    start = "AA"
    for line in data:
        s1, s2 = line.split("; ")
        rates[line[6:8]] = int(s1[s1.index("=") + 1 :])
        next_nodes[line[6:8]] = [v for v in s2.replace(",", "").split() if v.isupper()]

    distances = {node: {n: 1 for n in next_nodes[node]} for node in next_nodes}
    no_rate_nodes = [k for k in rates if rates[k] == 0]
    for node in no_rate_nodes:
        for n in rates:
            if node != n and node in distances[n]:
                for k in distances[node]:
                    if k != n:
                        if k in distances[n]:
                            distances[n][k] = min(
                                distances[n][k], distances[n][node] + distances[node][k]
                            )
                        else:
                            distances[n][k] = distances[n][node] + distances[node][k]
    if start in no_rate_nodes:
        start_nodes = []
        for n in next_nodes[start]:
            not_allowed = []
            visited = {start}
            if n in no_rate_nodes:
                not_allowed.append(n)
            else:
                start_nodes.append([n, 1])
            while not_allowed:
                node = not_allowed.pop(-1)
                visited.add(node)
                for k in next_nodes[node]:
                    if k not in visited:
                        if k in no_rate_nodes:
                            not_allowed.append(k)
                        else:
                            start_nodes.append([k, distances[start][node] + 1])
    else:
        start_nodes = [[start, 0]]

    for node in no_rate_nodes:
        for n in rates:
            if n == node:
                del distances[node]
            elif node in distances.get(n, []):
                del distances[n][node]

    rates = {k: v for k, v in rates.items() if v != 0}

    return rates, distances, start_nodes


def heuristic(open_nodes, rates, minutes_left):
    best_rates = sorted(
        [rates[n] for n in open_nodes if not open_nodes[n]], reverse=True
    )
    n = min(len(best_rates), minutes_left // 2 + 1)
    return sum(best_rates[i] * (minutes_left - 2 * i) for i in range(n))


def part_a(data):
    rates, distances, start_nodes = parse_data(data)
    minutes = 30
    best_solution = 0
    candidates = [
        ({n: False for n in rates}, start, minutes - m, 0) for start, m in start_nodes
    ]
    while candidates:
        open_nodes, current_node, minutes_left, current_value = candidates.pop(-1)
        if minutes_left <= 0:
            best_solution = max(best_solution, current_value)
            continue
        if current_value + heuristic(open_nodes, rates, minutes_left) < best_solution:
            continue
        for node, d in distances[current_node].items():
            candidates.append((open_nodes, node, minutes_left - d, current_value))
        if not open_nodes[current_node]:
            new_open_nodes = open_nodes.copy()
            new_open_nodes[current_node] = True
            minutes_left -= 1
            current_value += minutes_left * rates[current_node]
            for node, d in distances[current_node].items():
                candidates.append(
                    (new_open_nodes, node, minutes_left - d, current_value)
                )
    return best_solution


def heuristic2(open_nodes, rates, min_left, el_min_left):
    best_rates = sorted(
        [rates[n] for n in open_nodes if not open_nodes[n]], reverse=True
    )
    s = 0
    for i in range(len(best_rates)):
        if min_left <= 0 and el_min_left <= 0:
            break
        if min_left < el_min_left:
            s += best_rates[i] * el_min_left
            el_min_left -= 2
        else:
            s += best_rates[i] * min_left
            min_left -= 2
    return s


def part_b(data):
    rates, distances, start_nodes = parse_data(data)
    minutes = 26
    best_solution = 0
    candidates = [
        ({n: False for n in rates}, start, el_start, minutes - m, minutes - el_m, 0)
        for start, m in start_nodes
        for el_start, el_m in start_nodes
    ]
    while candidates:
        (
            open_nodes,
            curr_node,
            el_node,
            min_left,
            el_min_left,
            current_value,
        ) = candidates.pop(-1)
        if min_left <= 0 and el_min_left <= 0 or all(open_nodes.values()):
            best_solution = max(best_solution, current_value)
            continue
        if (
            current_value + heuristic2(open_nodes, rates, min_left, el_min_left)
            < best_solution
        ):
            continue
        new_open_nodes = open_nodes.copy()
        if min_left > 0 and el_min_left > 0:
            for cnode, cd in distances[curr_node].items():
                for elnode, eld in distances[el_node].items():
                    candidates.append(
                        (
                            new_open_nodes,
                            cnode,
                            elnode,
                            min_left - cd,
                            el_min_left - eld,
                            current_value,
                        )
                    )
            if not new_open_nodes[curr_node]:
                new_open_nodes[curr_node] = True
                min_left -= 1
                current_value += min_left * rates[curr_node]
                for cnode, cd in distances[curr_node].items():
                    for elnode, eld in distances[el_node].items():
                        candidates.append(
                            (
                                new_open_nodes,
                                cnode,
                                elnode,
                                min_left - cd,
                                el_min_left - eld,
                                current_value,
                            )
                        )
            if not new_open_nodes[el_node]:
                new_open_nodes[el_node] = True
                el_min_left -= 1
                current_value += el_min_left * rates[el_node]
                for cnode, cd in distances[curr_node].items():
                    for elnode, eld in distances[el_node].items():
                        candidates.append(
                            (
                                new_open_nodes,
                                cnode,
                                elnode,
                                min_left - cd,
                                el_min_left - eld,
                                current_value,
                            )
                        )
        elif min_left > 0:
            for node, d in distances[curr_node].items():
                candidates.append(
                    (
                        open_nodes,
                        node,
                        el_node,
                        min_left - d,
                        el_min_left,
                        current_value,
                    )
                )
            if not open_nodes[curr_node]:
                new_open_nodes[curr_node] = True
                min_left -= 1
                current_value += min_left * rates[curr_node]
                for node, d in distances[curr_node].items():
                    candidates.append(
                        (
                            new_open_nodes,
                            node,
                            el_node,
                            min_left - d,
                            el_min_left,
                            current_value,
                        )
                    )
        elif el_min_left > 0:
            for node, d in distances[el_node].items():
                candidates.append(
                    (
                        new_open_nodes,
                        curr_node,
                        node,
                        min_left,
                        el_min_left - d,
                        current_value,
                    )
                )
            if not new_open_nodes[el_node]:
                new_open_nodes = new_open_nodes.copy()
                new_open_nodes[el_node] = True
                el_min_left -= 1
                current_value += el_min_left * rates[el_node]
                for node, d in distances[el_node].items():
                    candidates.append(
                        (
                            new_open_nodes,
                            curr_node,
                            node,
                            min_left,
                            el_min_left - d,
                            current_value,
                        )
                    )
    return best_solution


aoc_data = get_data(day=DAY, year=YEAR).splitlines()
test_data = """\
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II""".splitlines()

if __name__ == "__main__":
    assert part_a(test_data) == 1651
    assert part_b(test_data) == 1706
    print(part_a(aoc_data))
    print(part_b(aoc_data))
