from collections import namedtuple
from typing import Iterator

def lines_generator() -> Iterator[str]:
    with open("input.txt", "r") as file:
        for line in file:
            yield line.rstrip()


Range = namedtuple('Range', "begin, end")

def ranges_generator():
    for line in lines_generator():
        first, second = line.split(',')
        first = Range(*map(int, first.split('-')))
        second = Range(*map(int, second.split('-')))
        yield first, second

def fully_contains(one: Range, other: Range) -> bool:
    return one.begin <= other.begin and \
        one.end >= other.end

def overlap(one: Range, other: Range) -> bool:
    return one.begin <= other.end and \
        one.end >= other.begin


def get_number_overlapping_pairs() -> int:
    return sum(
        1
        for first, second
        in ranges_generator()
        if overlap(first, second)
    )


def get_number_pairs_one_fully_contain_other() -> int:
    return sum(
        1
        for first, second
        in ranges_generator()
        if fully_contains(first, second)
        or fully_contains(second, first)
    )

def main() -> None:
    result = get_number_overlapping_pairs()
    print(result)


if __name__ == "__main__":
    main()
