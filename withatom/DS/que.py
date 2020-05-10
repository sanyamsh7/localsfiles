class QueueNode(object):
    def __init__(self, data, nxt):
        self.data = data
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.data
        return f"[{self.data} : {repr(nval)}]"

class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.cnt = 0

    def shift(self, obj):
        node = QueueNode(obj, None)
        self._invariants()
        self.cnt += 1
        if self.head == None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node

    def unshift(self):
        node = self.head
        if node:
            self.head = node.next
            return node.data
        else:
            self.cnt = 0
            return None

    def count(self):
        return self.cnt

    def dump(self, mark = "----"):
        node = self.head
        print(mark)
        while node:
            print(node, end = " ")
            node = node.next
        print()

    def _invariants(self):
        if self.count() == 0:
            assert self.head == None
            assert self.tail == None

        elif self.count() == 1:
            assert self.head == self.tail

        else:
            assert self.head != self.tail
