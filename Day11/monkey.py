import operator


class Monkey:
    def __init__(self) -> None:
        self.id = None
        self.items = None
        self.operation = self.operation_method
        self.test = self.test_method
        self.case_true = None
        self.case_false = None
        self.operator = None
        self.operand = None
        self.moduland = None
        self.count = 0

    def test_method(self, x):
        return x % int(self.moduland) == 0

    def operation_method(self, x):
        if self.operator == "+":
            gurke = operator.add
        else:
            gurke = operator.mul
        
        if self.operand == "old":
            y = x
        else:
            y = int(self.operand)
        # print("In operation", self.gurke, end="; ")
        return gurke(x, y)
    
    def inspect(self):
        self.count += 1
            
    
    