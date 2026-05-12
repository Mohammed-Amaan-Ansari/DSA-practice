from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)

        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0


if __name__ == "__main__":
    s = MyStack()

    s.push(1)
    s.push(2)

    print(s.top())    # 2
    print(s.pop())    # 2
    print(s.empty())  # False