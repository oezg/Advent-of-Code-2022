from functools import reduce


grid = []
with open("input.txt", "r") as file:
    for line in file:
        grid.append(list(map(int, line.rstrip())))


def solve_1():

    count = 2 * (len(grid) + len(grid[0]) - 2)

    for i, row in enumerate(grid[1:-1], 1):
        for j, num in enumerate(row[1:-1], 1):

            if all(map(lambda x: x < num, row[:j])) \
                or all(map(lambda x: x < num, row[j+1:])) \
                or all(map(lambda x: x < num, (grid[k][j] for k in range(i)))) \
                or all(map(lambda x: x < num, (grid[k][j] for k in range(i+1, len(grid))))):
                count += 1
                continue


    print(count)

solve_1()



def left(i, j):
    for k in range(j -1, -1, -1):
        yield 1
        if grid[i][k] >= grid[i][j]:
            return

def right(i, j):
    for k in range(j +1, len(grid[i])):
        yield 1
        if grid[i][k] >= grid[i][j]:
            return

def up(i, j):
    for k in range(i -1, -1, -1):
        yield 1
        if grid[k][j] >= grid[i][j]:
            return

def down(i, j):
    for k in range(i +1, len(grid)):
        yield 1
        if grid[k][j] >= grid[i][j]:
            return

def viewing_distances(i, j):
    return map(lambda direction: sum(direction(i, j)), [left, right, up, down])

def score(i,j):
    return reduce(lambda x, y: x * y, viewing_distances(i, j))

def viewing_scores():
    return map(lambda t: score(*t), ((i, j) for i in range(len(grid)) for j in range(len(grid[i]))))

def solve_2():
    return max(viewing_scores())

print(solve_2())