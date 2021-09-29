# Check if parentheses are balanced

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

class Deque(object):

    def __init__(self, arr):
        self.items = arr

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

# DOES NOT WORK FOR ASYMMETRICAL SETS
def balance_check(string):
    pairs = ['[]', '{}', '()']
    array_of_string = list(string)
    length = len(array_of_string)
    d = Deque(array_of_string)
    if (length % 2) == 1:
        return False
    while d.size() > 0:
        rear = d.remove_rear()
        front = d.remove_front()
        if rear + front not in pairs:
            return False
    return True


def balance_check2(string):
    s = Stack()
    if len(string) % 2 != 0:
        return False
    opening = '([{'
    pairs = ['[]', '{}', '()']
    for paren in string:
        if paren in opening:
            s.push(paren)
        else:
            if s.isEmpty():
                return False
            last_open = s.pop()
            if last_open + paren not in pairs:
                return False
    return True


print(balance_check2('[]()([[[]]])'))