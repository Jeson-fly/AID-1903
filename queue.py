'''
队列的构造
'''
from collections import deque #双向队列

class Queue(object):
    def __init__(self, size):
        self.size = size
        self.queue = [0 for _ in range(self.size)]
        self.rear = 0
        self.front = 0

    # 入队
    def push(self, element):
        if self.is_filled():
            raise IndexError("Queue is filled")
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = element

    # 出队
    def pop(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        self.front = (self.front + 1) % self.size
        return self.queue[self.front]

    # 队空
    def is_empty(self):
        # if self.front==self.rear:
        #     return True
        # return False
        return self.front == self.rear

    # 队满
    def is_filled(self):
        # if self.front==(self.rear+1)%self.size:
        #     return True
        # return False
        return self.front == (self.rear + 1) % self.size

    # 查看队首元素
    def get_front_element(self):
        front = (self.front + 1) % self.size
        return self.queue[front]

    # 查看队尾元素
    def get_rear_element(self):
        return self.queue[self.rear]


if __name__ == "__main__":
    # queue=Queue(10)
    # for i in range(9):
    #     queue.push(i)
    # print(queue.pop())
    q = deque()
    q.append(1)
    print(q.popleft())