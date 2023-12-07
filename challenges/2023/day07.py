from aocd import get_data

DAY, YEAR = 7, 2023


class Hand:
    def __init__(self, cards):
        self.cards_str = cards
        self.cards = [int(card) if card.isdigit() else 10 + "TJQKA".index(card) for card in cards]

        set_cards = set(cards)

        if len(set_cards) == 1:
            self.rank = 6
            return

        if len(set_cards) == 2 and cards.count(cards[0]) in (1, 4):
            self.rank = 5
            return

        if len(set_cards) == 2:
            self.rank = 4
            return

        # Check for three of a kind
        if len(set_cards) == 3 and cards.count(cards[0]) in (1, 3) and cards.count(cards[1]) in (1, 3):
            self.rank = 3
            return

        if len(set_cards) == 3:
            self.rank = 2
            return

        if len(set_cards) == 4:
            self.rank = 1
            return

        self.rank = 0

    def __gt__(self, other):
        if self.rank == other.rank:
            for i in range(len(self.cards)):
                if self.cards[i] > other.cards[i]:
                    return True
                elif self.cards[i] < other.cards[i]:
                    return False
            return False
        return self.rank > other.rank

    def __lt__(self, other):
        if self.rank == other.rank:
            for i in range(len(self.cards)):
                if self.cards[i] < other.cards[i]:
                    return True
                elif self.cards[i] > other.cards[i]:
                    return False
            return False
        return self.rank < other.rank

    def __repr__(self):
        return self.cards_str


class HandB(Hand):
    def __init__(self, cards):
        super().__init__(cards)
        self.cards = [1 if card == 11 else card for card in self.cards]
        jokers = self.cards.count(1)
        if jokers:
            new_rank = self.rank + jokers
            if self.rank == jokers == 3:
                new_rank = 5
            elif self.rank == 2 and jokers == 1:
                new_rank = 4
            elif new_rank in (2, 4):
                new_rank += 1
            self.rank = min(new_rank, 6)


def part_a(data):
    data = [(Hand(line.split()[0]), int(line.split()[1])) for line in data]
    ranks = sorted(data, key=lambda x: x[0])
    return sum(bid * (i + 1) for i, (_, bid) in enumerate(ranks))


def part_b(data):
    data = [(HandB(line.split()[0]), int(line.split()[1])) for line in data]
    ranks = sorted(data, key=lambda x: x[0])
    return sum(bid * (i + 1) for i, (_, bid) in enumerate(ranks))


aoc_data = get_data(day=DAY, year=YEAR).splitlines()
test_data = """\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".splitlines()

if __name__ == "__main__":
    assert part_a(test_data) == 6440
    assert part_b(test_data) == 5905
    print(part_a(aoc_data))
    print(part_b(aoc_data))
