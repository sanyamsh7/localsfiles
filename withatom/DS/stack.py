class StackNode(object):
    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value} : {repr(nval)}]"

class Stack(object):

    def __init__(self):
        self.top = None
        self.cnt = 0

    def push(self, obj):
        """pushes a new value to the top of the stack."""
        self._invariant()
        self.cnt += 1
        node = StackNode(obj, None)
        if self.top == None:
            self.top = node
            
        else:
            node.next = self.top
            self.top = node

    def pop(self):
        """Pops the value that is currently on the top of the stack."""
        self._invariant()
        self.cnt -= 1
        if self.top == None:
            self.cnt = 0
            return None
        else:
            node = self.top
            self.top = self.top.next
            return node.value

    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        return self.top and self.top.value

    def count(self):
        """Counts the number of elements in the stack."""
        return self.cnt

    def _invariant(self):
        if self.cnt == 1:
             assert self.top.next == None
        elif self.cnt == 0:
            assert self.top == None
        assert self.cnt != -1
