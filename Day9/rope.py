from node import Node


class Rope:
    def __init__(self, num_nodes) -> None:
        self.head = Node()
        current = self.head
        for _ in range(num_nodes-1):
            current.next_node = Node()
            current = current.next_node
        self.tail = current

    def pull(self, dx: int, dy: int) -> None:
        for _ in range(abs(dx)):
            self.head.move(dx//abs(dx), 0)
        for _ in range(abs(dy)):
            self.head.move(0, dy//abs(dy))
            

    def pprint(self):
        ptr = self.head
        ctr = 0
        grd = []
        for _ in range(20):
            row = []
            for _ in range(40):
                row.append("_")
            grd.append(row)

        while ptr:
            grd[10-ptr.y][20+ptr.x] = str(ctr)
            ctr += 1
            ptr = ptr.next_node
        
        for row in grd:
            print(" ".join(row))
        print('-'*40)
            


