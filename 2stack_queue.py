# Create queue using 2 stacks

class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)


# Works only if entire set is passed during enqueue before any dequeueing
class Queue2Stacks(object):

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, element):
        for item in element:
            self.stack1.push(item)
        while not self.stack1.isEmpty():
            current = self.stack1.pop()
            self.stack2.push(current)
        return self.stack2

    def dequeue(self):
        return self.stack2.pop()


# Works better if enqueueing is happening randomly
# instead of all at once at the beginning
class Queue2Stacks2(object):

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, element):
        self.stack1.push(element)

    def dequeue(self):
        while not self.stack1.isEmpty():
            current = self.stack1.pop()
            self.stack2.push(current)
        answer = self.stack2.pop()
        while not self.stack2.isEmpty():
            current = self.stack2.pop()
            self.stack1.push(current)
        return answer


queue = Queue2Stacks2()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())
queue.enqueue(5)
queue.enqueue(6)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())