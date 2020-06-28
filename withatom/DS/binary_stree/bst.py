class Node(object):
    def __init__(self, key, value, left = None, right = None, parent = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def minimum(self):
        """get minimum"""
        node = self
        while node.left:
            node = node.left
        return node

    def replace_node_in_parent(self, child):
        if self.parent:
            if self == self.parent.left:
                self.parent.left = child
            else:
                self.parent.right = child

        if child:
            child.parent = self.parent

    def __repr__(self):
        return f"{self.key}={self.value}:<---left({self.left}) --->right({self.right})"

class Tree(object):
    def __init__(self):
        self.root = None

    def __search(self, node, key):
        if node == None:
            return None
        elif node.key == key:
            return node.value
        elif node.left == None and node.right == None:
             return None
        else:
            if key < node.key:
                return self.__search(node.left, key)
            elif key > node.key:
                return self.__search(node.right, key)

    def __insert(self, node, key, value):
        if self.root == None:
            self.root = Node(key, value)

        elif node.key == key:
            node.value = value

        else:
            if key < node.key:
                if node.left:
                    self.__insert(node.left, key, value)
                else:
                    node.left = Node(key, value)

            elif key > node.key:
                if node.right:
                    self.__insert(node.right, key, value)
                else:
                    node.right = Node(key, value)

    def __delete(self, node, key):
        if key < node.key:
            self.__delete(node.left, key)
        if key > node.key:
            self.__delete(node.right, key)
        else:
            #node has both children
            if node.left and node.right:
                successor = node.right.minimum()
                node.key = successor.key
                self.__delete(successor, successor.key)
            #node has left child
            elif node.left:
                if self.root == node:
                    self.root = node.left
                else:
                    node.replace_node_in_parent(node.left)
            #node had right child
            elif node.right:
                if self.root == node:
                    self.root = node.right
                else:
                    node.replace_node_in_parent(node.right)
            else:
                #node has no child
                if self.root == node:
                    self.root = None
                else:
                    node.replace_node_in_parent(None)

    def get(self, key):
         if self.root:
             return self.__search(self.root, key)

    def set(self, key, value):
        self.__insert(self.root, key, value)

    def delete(self, key):
        if self.root:
            self.__delete(self.root, key)
        else:
            return None
