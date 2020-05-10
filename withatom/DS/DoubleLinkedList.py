class DLLNode(object):
    def __init__(self, prev, data, nxt):
        self.prev = prev
        self.data = data
        self.next = nxt
    def __repr__(self):
        nval = self.next and self.next.data or None
        pval = self.prev and self.prev.data or None
        return f"[{repr(pval)}, {self.data}, {repr(nval)}]"

class DoubleLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.cnt = 0

    def push(self, obj):
        self._invariant()
        node = DLLNode(None, obj, None)
        self.cnt += 1
        if self.head == None:
            self.head = node
            self.tail = self.head
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            assert self.head != self.tail

    def pop(self):
        self._invariant()
        self.cnt -= 1
        if self.head == None:
            self.cnt = 0
            return None
        elif self.head == self.tail:
            node = self.head
            self.head = self.tail = None
            return node.data
        else:
            node = self.tail
            self.tail = node.prev
            self.tail.next = None
            return node.data
#rebuild this function
    def shift(self, obj):
        self._invariant()
        node = DLLNode(None, obj, None)
        self.cnt +=1
        if self.head == None:
            self.head = node
            self.tail = self.head
        else:
            self.head.next = None   ###important next of last should be None
            node.next = self.head
            self.head.prev = node
            self.head = node

    def unshift(self):
        self.cnt -= 1
        if self.head == None:
            self.cnt = 0
            self.tail = None
            self._invariant()
            return None
        else:
            node = self.head
            self.head = node.next

            return node.data

    def count(self):
        return self.cnt

    def first(self):
        return self.head.data

    def last(self):
        return self.tail.data

    def detach(self, node):
        if node.next == None:
            node.prev.next = None
            self.tail = node.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self._invariant()

    def remove(self, match):
        node = self.head
        index = 0
        self._invariant()
        if node == None:
            return None

        elif node.data == match and node.next == None:
            self.head = self.tail = None
            return (index)

        elif node.data == match and node.next != None:
            self.head = node.next
            self.head.prev = None
            return (index)

        else:
            while node.data != match:
                node = node.next
                index+=1
            self.detach(node)
            return (index)


    def get(self, index):
        i = 0
        #print("inside get :")
        if self.cnt == index:
            return None
        else:
            #print("else of get:")
            node = self.head
            #print("node:", node)
            while i!=index:
                node = node.next
                #print("node: ", node)
                i+=1
                #print("i:", i)
            #print("return node:", node)
            return node.data

    def _invariant(self):
        if self.cnt == 0:
            assert self.head == None
            assert self.tail == None
        elif self.cnt == 1:
            assert self.head == self.tail
        elif self.head == None:
            assert self.tail == None
        else:
            assert self.head.prev == None
            assert self.tail.next == None

    def dump(self, mark):
        pass
