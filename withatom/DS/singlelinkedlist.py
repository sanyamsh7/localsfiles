#understanding single nexted lists:

class SingleLinkedListNode(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None

        return f"[{self.value} : {repr(nval)}]"

class SingleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None
        self.cnt = 0

    def push(self, obj):
        """Appends a new value on the end of the list."""
        self.cnt += 1
        new_node = SingleLinkedListNode(obj, None)
        if self.begin == None:
            self.begin = new_node
            self.end = self.begin
        else:
            self.end.next = new_node
            self.end = new_node
            assert self.begin != self.end
        assert self.end.next == None

    def pop(self):
        """Removes the last item and returns it."""
        self.cnt -= 1
        if self.end == None:
            return None
        elif self.end == self.begin:
            node = self.begin
            self.end = self.begin = None
            return node.value
        else:
            node = self.begin
            while node.next != self.end: #this is for traversal of all the nodes
                node = node.next
            assert self.end != node
            self.end = node
            return node.next.value

    def shift(self, obj):
        """Another name for push."""
        self.cnt+=1
        node = SingleLinkedListNode(obj, None)
        if self.begin == None:
            self.begin = node
            self.end = self.begin
        else:
            node.next = self.head
            self.head = node

    def unshift(self):
        """Removes the first item and returns it."""
        self.cnt -= 1          #if unshift is called without pushing or shifting it will return -1
        if self.begin == None:
            return None
        else:
            node = self.begin
            self.begin = node.next
            return node.value

    def remove(self, obj):
        """Finds a matching item and removes it from the list."""
        node = self.begin
        index = 0
        if node.value == obj:
            self.begin = node.next
            return index
        else:
            while node.next.value != obj:
                node = node.next
                index += 1
            index += 1
            return index

    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        return self.begin.value

    def last(self):
        """Returns a reference to the last item, does not remove."""
        return self.end.value

    def count(self):
        """Counts the number of elements in the list."""
        return self.cnt

    def get(self, index):
        """Get the value at index."""
        node = self.begin
        i = 0
        if index == self.cnt:
            return None
        else:
            while i != index:
                node = node.next
                i+=1
            return node.value

    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""
        pass
