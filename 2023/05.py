from typing import Tuple


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data: str):
    input_data = input_data.strip()
    lines = [line.strip().split(":")[1] for line in input_data.split("\n\n")]
    seeds = [int(n) for n in lines[0].split()]

    maps = []
    for line in lines[1:]:
        map_data = [[int(n) for n in li.split()] for li in line.strip().split("\n")]
        maps.append(map_data)

    return seeds, maps


def map_seed(seed: int, map: list[list[int]]):
    for m in map:
        dst, src, r = m
        if src <= seed < src + r:
            return dst + seed - src
    return seed


def map_seed_range(seed_range: list[Tuple[int, int]], map):
    result = []
    for dst, map_start, r in map:
        map_end = map_start + r
        seeds_ooo = []
        while seed_range:
            seed_start, seed_end = seed_range.pop()

            before = (seed_start, min(seed_end, map_start))
            in_range = (max(seed_start, map_start), min(seed_end, map_end))
            after = (max(seed_start, map_end), seed_end)

            if before[1] > before[0]:
                seeds_ooo.append(before)
            if in_range[1] > in_range[0]:
                result.append(
                    (in_range[0] + dst - map_start, in_range[1] + dst - map_start)
                )
            if after[1] > after[0]:
                seeds_ooo.append(after)

        seed_range = seeds_ooo
    return seed_range + result


def part_1(input_data: str) -> int:
    seeds, maps = parse(input_data)
    result = []
    for s in seeds:
        for m in maps:
            s = map_seed(s, m)
        result.append(s)
    return min(result)


def part_2(input_data: str) -> int:
    seeds, maps = parse(input_data)
    seed_pairs = list(zip(seeds[::2], seeds[1::2]))
    result = []
    for seed_start, seed_range_size in seed_pairs:
        seed_range = [(seed_start, seed_start + seed_range_size)]
        for m in maps:
            seed_range = map_seed_range(seed_range, m)
        result.append(min(seed_range)[0])
    return min(result)


if __name__ == "__main__":
    input_data = read_input("inputs/2023/day5.txt")
    print(part_1(input_data))
    print(part_2(input_data))


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
    input_data = read_input("inputs/2023/day5.txt")
    assert part_1(input_data) == 535088217


def test__part2_sample():
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

    assert part_2(sample) == 46


def test__part2():
    input_data = read_input("inputs/2023/day5.txt")
    assert part_2(input_data) == 51399228
