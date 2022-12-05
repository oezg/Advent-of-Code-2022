from typing import Iterator

def lines_generator() -> Iterator[str]:
    with open("input.txt", "r") as file:
        for line in file:
            yield line.rstrip()

def main():
    result = 
    print(result)


if __name__ == "__main__":
    main()

