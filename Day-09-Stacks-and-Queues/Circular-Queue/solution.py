class MyCircularQueue:

    def __init__(self, k):
        self.queue = [0] * k
        self.head = 0
        self.count = 0
        self.capacity = k

    def enQueue(self, value):
        if self.isFull():
            return False

        tail = (self.head + self.count) % self.capacity
        self.queue[tail] = value
        self.count += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False

        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self):
        return -1 if self.isEmpty() else self.queue[self.head]

    def Rear(self):
        return -1 if self.isEmpty() else self.queue[(self.head + self.count - 1) % self.capacity]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.capacity


if __name__ == "__main__":
    q = MyCircularQueue(3)

    print(q.enQueue(1))
    print(q.enQueue(2))
    print(q.enQueue(3))
    print(q.isFull())
    print(q.Rear())