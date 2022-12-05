import re
from collections import deque
from collections import defaultdict
from string import ascii_uppercase
from typing import Iterator

def lines_generator() -> Iterator[str]:
    with open("input.txt", "r") as file:
        for line in file:
            yield line.rstrip()

def main():
    stacks = defaultdict(deque)
    crates = deque()
    moves = deque()
    cratemover = deque()
    change = False
    
    # Get crates and moves
    for line in lines_generator():
        if change:
            moves.append(line)
        elif not line:
            change = True
        else:
            crates.append(line)
    
    
    stack_numbers: str = crates.pop()
    stack_ids: dict[str, int] = {
        stack_id: stack_numbers.index(stack_id)
        for stack_id in stack_numbers.split()
    }

    while crates:
        level: str = crates.pop()
        for i, ch in enumerate(level):
            if ch in ascii_uppercase:
                stacks[i].append(ch)
    
    pattern_string = re.compile(r"move (\d+) from (\d+) to (\d+)")

    while moves:
        move = moves.popleft()
        amount, from_stack, to_stack = pattern_string.match(move).groups()
        to_stack = stacks[stack_ids[to_stack]]
        from_stack = stacks[stack_ids[from_stack]]
        
        for _ in range(int(amount)):
            cratemover.appendleft(from_stack.pop())
        while cratemover:
            to_stack.append(cratemover.popleft())

        #     Part 1 Solution
        #     to_stack.append(from_stack.pop())


    result = "".join(stack.pop() for stack in stacks.values())
    print(result)


if __name__ == "__main__":
    main()

