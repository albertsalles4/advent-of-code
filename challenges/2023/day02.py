from aocd import get_data

DAY, YEAR = 2, 2023


def parse_data(data):
    games = {}
    for line in data:
        game = []
        game_name, line = line.split(": ")
        game_id = int(game_name.split()[1])
        for sets in line.split("; "):
            game_set = {}
            cubes = sets.split(", ")
            for cube in cubes:
                num, colour = cube.split()
                game_set[colour] = int(num)
            game.append(game_set)
        games[game_id] = game

    return games


def part_a(data):
    games = parse_data(data)
    max_balls = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    s = 0
    for game_id, game in games.items():
        possible = True
        i = 0
        while possible and i < len(game):
            possible = game[i].get("red", 0) <= max_balls["red"] and \
                       game[i].get("green", 0) <= max_balls["green"] and \
                       game[i].get("blue", 0) <= max_balls["blue"]
            i += 1

        if possible:
            s += game_id

    return s


def part_b(data):
    games = parse_data(data)
    s = 0
    for game_id, game in games.items():
        mins = {
            "red": 1,
            "green": 1,
            "blue": 1,
        }

        for game_set in game:
            for colour in ["red", "green", "blue"]:
                if colour in game_set:
                    mins[colour] = max(mins[colour], game_set[colour])
        s += mins["red"] * mins["green"] * mins["blue"]

    return s


aoc_data = get_data(day=DAY, year=YEAR).splitlines()
test_data = """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""".splitlines()

if __name__ == "__main__":
    assert part_a(test_data) == 8
    assert part_b(test_data) == 2286
    print(part_a(aoc_data))
    print(part_b(aoc_data))
