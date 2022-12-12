import re
from operator import add, mul
import typing
from monkey import Monkey


def make_monkeys():
    with open("test.txt") as f:
        lines = [line.strip() for line in f]
    
    monkeys = []

    for line in lines:
        if line.startswith("Monkey"):
            monkey = Monkey()
            monkeys.append(monkey)
            monkey.id = re.search("\d", line).group()
        elif line.startswith("Starting"):
            monkey = monkeys[-1]
            monkey.items = [
                int(item) for item in
                line.split(":")[1].split(",")
            ]
        elif line.startswith("Operation"):
            monkey = monkeys[-1]
            _, monkey.operator, monkey.operand = line.split("=")[1].split()
        elif line.startswith("Test"):
            monkey = monkeys[-1]
            monkey.moduland = line.split()[-1]
        elif line.startswith("If true"):
            monkey = monkeys[-1]
            monkey.case_true = line.split()[-1]
        elif line.startswith("If false"):
            monkey = monkeys[-1]
            monkey.case_false = line.split()[-1]
        else:
            pass
    return monkeys

def one_round(monkeys):
    for monkey in monkeys:
        # print(f"Before {monkey.id} turn:", monkey.items)
        while monkey.items:
            # print("1", len(monkey.items), end=", ")
            item = monkey.items.pop(0)
            # print("2", item, end=", ")
            monkey.inspect()
            value = monkey.operation(item)
            # print("3", value, end=", ")
            # value = int(value / (23*19*13*17))
            # print("4", value, end=", ")
            if monkey.test(value):
                target = int(monkey.case_true)
            else:
                target = int(monkey.case_false)
            # print("5", target)
            monkeys[target].items.append(value)
    # for monkey in monkeys:
    #     print(f"Monkey {monkey.id}:", monkey.count)

def main():
    monkeys = make_monkeys()
    for i in range(20):
        # print("After round", i+1)
        one_round(monkeys)
    # print(monkeys[0].items)
    result = sorted((monkey.count for monkey in monkeys), reverse=True)
    print(mul(*result[:2]))
    for m in monkeys:
        print("Monkey", m.id, "inspected", m.count)


if __name__ == "__main__":
    main()

