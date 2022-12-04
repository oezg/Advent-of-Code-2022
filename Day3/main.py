import string

priority_string = string.ascii_lowercase + string.ascii_uppercase

def priority(character) -> int:
    if len(character) == 1:
        return 1 + priority_string.index(character)


def lines_generator():
    with open("input.txt", "r") as file:
        for line in file:
            yield line.rstrip()

def item_types_generator():
    for line in lines_generator():
        middle = len(line) // 2
        yield set(
            line[:middle]
        ).intersection(
            line[middle:]
        )

def find_sum_priorities():
    return sum(
        priority(*item_type)
        for item_type in item_types_generator()
    )

def groups_generator():
    group = list()
    for line in lines_generator():
        group.append(line)
        if len(group) == 3:
            yield group
            group.clear()

def badges_generator():
    for group in groups_generator():
        yield set(group[0]).intersection(
            group[1]
        ).intersection(
            group[2]
        )

def sum_priorities_of_badges():
    return sum(
        priority(*badge)
        for badge in badges_generator()
    )

def main():
    result = sum_priorities_of_badges()
    print(result)


if __name__ == "__main__":
    main()

