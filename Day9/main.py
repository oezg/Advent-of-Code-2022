from typing import Iterator
from rope import Rope

def lines_generator() -> Iterator[str]:
    with open("input.txt", "r") as file:
        for line in file:
            yield line.rstrip()

def main():
    rope = Rope(10)

    for line in lines_generator():
        direction, step = line.split()
        step = int(step)
        match direction:
            case "R":
                rope.pull(step, 0)
            case "L":
                rope.pull(-step, 0)
            case "U":
                rope.pull(0, step)
            case "D":
                rope.pull(0, -step)
        
        # rope.pprint()
    print(len(rope.tail.positions))


if __name__ == "__main__":
    main()

