import math


class Node:
    def __init__(self, x: int = 0, y:int = 0) -> None:
        self.x = x
        self.y = y
        self.next_node = None
        self.positions = {(self.x, self.y)}

    def move(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy
        if self.next_node:
            if abs(self.x - self.next_node.x) > 1 or abs(self.y - self.next_node.y) > 1:
                _x = math.ceil(abs(self.x - self.next_node.x) / 2) * Node.sign(self.x - self.next_node.x)
                _y = math.ceil(abs(self.y - self.next_node.y) / 2) * Node.sign(self.y - self.next_node.y)
                self.next_node.move(_x, _y)
        else:
            self.positions.add((self.x, self.y))

    def sign(x):
        return -1 if x < 0 else 1
