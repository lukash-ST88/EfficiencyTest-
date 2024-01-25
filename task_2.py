# First in First out

class IndexListQueue:
    def __init__(self, size):
        self.list = [0] * size
        self.head = 0
        self.tail = 0
        self.amount = 0
        self.size = size

    def push(self, item):
        if self.amount == self.size:
            raise Exception("Queue is full, it should be extended")

        self.list[self.head] = item

        self.amount += 1
        self.head = self.next(self.head)

    def pop(self):
        if self.amount == 0:
            raise Exception("Queue is empty! Fill the queue by method push.")

        item = self.list[self.tail]

        self.amount -= 1

        self.tail = self.next(self.tail)
        return item

    def next(self, index):
        next_index = index + 1
        return 0 if next_index >= self.size else next_index


class LinkedListQueue:
    def __init__(self, size):
        self.size = size
        self.amount = 0
        item = LinkedListItem()
        first = item
        for i in range(size - 1):
            item = LinkedListItem(item)
        first.next_item = item
        self.head = first
        self.tail = first

    def push(self, item):
        if self.amount == self.size:
            raise Exception("Queue is full, it should be extended")
        self.head.data = item
        self.amount += 1
        self.head = self.head.next_item

    def pop(self):
        if self.amount == 0:
            raise Exception("Queue is empty! Fill the queue by method push.")
        item = self.tail.data
        self.amount -= 1
        self.tail = self.tail.next_item
        return item


class LinkedListItem:
    def __init__(self, next_item=None):
        self.data = 0
        self.next_item = next_item
