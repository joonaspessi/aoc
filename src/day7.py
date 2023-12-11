from collections import Counter
from dataclasses import dataclass

card_to_value = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


@dataclass
class Card:
    index: int
    value: int


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid

    @property
    def value(self):
        c = Counter(self.cards)
        max_value = max(c.values())
        if max_value == 5:
            return 7
        if max_value == 4:
            return 6
        if 3 in c.values() and 2 in c.values():
            return 5
        if max_value == 3:
            return 4
        # two pairs
        if len(c) == 3:
            return 3
        # pair
        if len(c) == 4:
            return 2
        # high card
        if len(c) == 5:
            return 1
        assert False, "should not get here"

    def __repr__(self):
        return f"{str(self.cards)} value: {self.value}"

    def __lt__(self, other):
        if self.value == other.value:
            for i in range(len(self.cards)):
                if self.cards[i] == other.cards[i]:
                    continue
                return self.cards[i] < other.cards[i]
            assert False, "should not get here"
        return self.value < other.value


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data: str, part_2=False):
    lines = [line.strip().split(" ") for line in input_data.strip().split("\n")]
    hands = []
    for cards, bid in lines:
        c = []
        for i, card in enumerate(cards):
            c.append(card_to_value[card])
        hands.append(Hand(c, int(bid)))
    return hands


def part_1(input_data: str) -> int:
    hands = parse(input_data)
    result = 0
    for i, hand in enumerate(sorted(hands)):
        result += hand.bid * (i + 1)
        print(i + 1)
    return result


if __name__ == "__main__":
    input_data = read_input("inputs/day7.txt")
    print(f"part1: {part_1(input_data)}")


def test__part_sample():
    sample = """
        32T3K 765
        T55J5 684
        KK677 28
        KTJJT 220
        QQQJA 483
    """
    assert part_1(sample) == 6440


def test__part1():
    assert part_1(read_input("inputs/day7.txt")) == 246795406
