class BSTreeNode(object):
    def __init__(self, key, value, left = None, right = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.key}={self.value}:<---left({self.left}) --->right({self.right})"

class BSTree(object):
    def __init__(self):
        self.root = None

    def set(self, key, value):
        if self.root == None:
            self.root = BSTreeNode(key, value)
        else:
            node = self.root
            while node:
                #if key is similar replace
                if node.key == key:
                    node.value = value
                    break
                #when leaf is found
                elif node.left == None and node.right == None:
                    if key < node.key:
                        node.left = BSTreeNode(key, value)
                    else:
                        node.right = BSTreeNode(key, value)
                #whrn leaf is not found
                else:
                    if key < node.key:
                        #if left of node is not None
                        if node.left:
                            node = node.left
                        else:
                            node.left = BSTreeNode(key, value)
                    else:
                        #if right of found node is not None
                        if node.right:
                            node = node.right
                        else:
                            node.right = BSTreeNode(key, value)

    def get(self, key):
        if not self.root:
            return None
        node = self.root
        while node:
            if node.key == key:
                return node.value

            elif node.left == None and node.right == None:
                return None

            elif key < node.key:
                node = node.left

            elif key >= node.key:
                node = node.right

    def _list(self, node, indent=0):
        """List the elements in the tree."""
        assert node, "Invalid node given."

        if node:
            print(" " * indent, node.key,"=", node.value)

            if node.left:
                print(" " * indent, "<", end="")
                self._list(node.left, indent+1)
            if node.right:
                print(" " * indent, ">", end="")
                self._list(node.right, indent+1)

    def list(self, start=""):
        print("\n\n----", start)
        self._list(self.root)
