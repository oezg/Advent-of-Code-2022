"""
Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
"""

def main():
    # read calories
    with open("input.txt", "r") as file:
        lines = file.readlines()
    
    max_elf = 0
    current_elf = 0
    for line in lines:
        if line.isspace():
            if current_elf > max_elf:
                max_elf = current_elf
            current_elf = 0
        else:
            current_elf += int(line)
    print(max_elf)



if __name__ == "__main__":
    main()

