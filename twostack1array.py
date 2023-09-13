import math

class TwoStacks:

    def __init__(self, n):
        self.size = n
        self.arr = [None] * n  # Initialize the array with None values
        self.top1 = math.floor(n / 2) + 1
        self.top2 = math.floor(n / 2)

    def push1(self, x):
        if self.top1 > 0:
            self.top1 = self.top1 - 1
            self.arr[self.top1] = x
        else:
            print("stack overflow")

    def push2(self, x):
        if self.top2 < self.size - 1:
            self.top2 = self.top2 + 1
            self.arr[self.top2] = x
        else:
            print("stack overflow")

    def pop1(self):
        if self.top1 <= self.size / 2:
            x = self.arr[self.top1]
            self.top1 = self.top1 + 1
            return x
        else:
            print("stack underflow")
            exit()

    def pop2(self):
        if self.top2 >= math.floor(self.size / 2) + 1:
            x = self.arr[self.top2]
            self.top2 = self.top2 - 1
            return x
        else:
            print("underflow")
            exit()

ts = TwoStacks(5)
ts.push1(5)
ts.push2(10)
ts.push2(15)
ts.push1(11)
ts.push2(7)

print("Popped element from stack1 is : " + str(ts.pop1()))
ts.push2(40)
print("Popped element from stack2 is : " + str(ts.pop2()))
