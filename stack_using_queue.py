from collections import deque
class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        v = len(self.q) - 1
        i = 0
        while i < v:
            self.q.append(self.q.popleft())
            i += 1

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0
      
myStack = MyStack();
print(myStack.push(1))
print(myStack.push(2))
print(myStack.top())
print(myStack.pop())
print(myStack.empty())