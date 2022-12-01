"""
Part 1:
Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

Part 2:
Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
"""

def main():
    # read calories
    with open("input.txt", "r") as file:
        lines = file.readlines()
    
    def elf_generator(lines: list[str]):
        elf = []
        for line in lines:
            if not line.isspace():
                elf.append(int(line))
            else:
                yield elf
                elf = []

    def find_maximum_n(n: int=1) -> int:
        elfgen = elf_generator(lines=lines)
        return sum(
            sorted(
                sum(elf) for elf in elfgen
            )[-n:]
        )
    
    def find_maximum() -> int:
        max_elf = 0
        current_elf = 0
        for line in lines:
            if line.isspace():
                if current_elf > max_elf:
                    max_elf = current_elf
                current_elf = 0
            else:
                current_elf += int(line)
        return max_elf

    result = find_maximum_n(3)
    print(result)




if __name__ == "__main__":
    main()

