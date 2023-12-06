def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def map_seed(seed: int, map_data):
    for dest, source, r in map_data:
        if seed in range(source, source + r):
            return dest + seed - source
    return seed


def parse(input_data: str):
    input_data = input_data.strip()
    lines = [line.strip().split(":")[1] for line in input_data.split("\n\n")]
    seeds = [int(n) for n in lines[0].split()]

    for line in lines[1:]:
        map_data = [[int(n) for n in li.split()] for li in line.strip().split("\n")]
        for i, s in enumerate(seeds):
            seeds[i] = map_seed(s, map_data)

    return seeds


def part_1(input_data: str) -> int:
    seeds = parse(input_data)
    return min(seeds)


if __name__ == "__main__":
    input_data = read_input("inputs/day5.txt")
    print(part_1(input_data))
    # print(part_2(input_data))


def test__part1_sample():
    sample = """
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
    """

    assert part_1(sample) == 35


def test__part1():
    input_data = read_input("inputs/day5.txt")
    assert part_1(input_data) == 535088217
