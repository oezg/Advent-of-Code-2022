from functools import reduce

def get_lines():
    with open("input.txt") as f:
        for line in f:
            yield line.lstrip()


crt = [False]*240

def show_crt():
    width = len(crt) // 6
    for i in range(1, 7):
        begin = (i-1)*width
        end = i * width
        stringify = ("#" if bl else "." for bl in crt[begin:end])
        row = " ".join(stringify)
        print(row)

def mark_crt():
    register = get_register()
    i = 0
    while i < len(crt):
        num = register[i]
        if abs(num - i % 40) < 2:
            crt[i] = True
        i += 1

def get_register():
    lines = get_lines()
    register = [0] * 240
    register[0] = 1

    clock = 0
    skip = False
    while clock < len(register) - 1:
        clock += 1
        register[clock] += register[clock - 1]

        if skip:
            skip = False
            continue

        line = next(lines)
        if not line.startswith('noop'):
            skip = True
            number = int(line.split()[1])
            register[clock + 1] += number
    return register

def solve_1():
    lines =get_lines()
    sums = []
    clock = 0
    register = [0] * 240
    register[0] = 1
    critical = [20, 60, 100, 140, 180, 220]
    i = 0
    skiponetick=False
    while i < len(critical):
        clock += 1
        if clock == critical[i]:
            sums.append(sum(register[:clock]))
            i += 1
        if skiponetick:
            skiponetick = False
            continue
        line = next(lines)
        if not line.startswith("noop"):
            skiponetick = True
            number = int(line.split()[1])
            register[clock+1] += number
    return reduce(lambda x, y: x + y, map(lambda x, y: x*y, sums, critical), 0)
        
def main():
    mark_crt()
    show_crt()


if __name__ == "__main__":
    main()

