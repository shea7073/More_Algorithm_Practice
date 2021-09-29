# Checking if a linked list is circular, takes a node

class Node(object):

    def __init__(self, value):

        self.value = value
        self.next_node = None


def cycle_check(node):
    first = node
    if node.next_node is None:
        return False
    current = node.next_node
    while current != first:
        if current.next_node is None:
            return False
        else:
            current = current.next_node
    return True


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e
# e.next_node = a

# singly_list = [a, b, c, d]

print(cycle_check(e))