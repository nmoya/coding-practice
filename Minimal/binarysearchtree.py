#!/usr/bin/python
import Queue

class Node():

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree():

    def __init__(self):
        self.root = None

    def _insert(self, node, parent, newnode):
        if node is None:  # Leaf node
            if self.root is None:
                self.root = newnode
            else:
                if newnode.value <= parent.value:
                    parent.left = newnode
                else:
                    parent.right = newnode
        else:  # Not a leaf
            if newnode.value <= node.value:
                self._insert(node.left, node, newnode)
            else:
                self._insert(node.right, node, newnode)

    def insert(self, newnode):
        ''' Inserts a new node in the binary search tree. Nodes smaller
        than the root are on the left, greater on the right '''
        self._insert(self.root, None, newnode)

    def _preorder(self, node):
        if node is None:
            return
        else:
            print node.value
            self._preorder(node.left)
            self._preorder(node.right)

    def preorder(self):
        ''' Visit the node, go left, and go right '''
        self._preorder(self.root)

    def _inorder(self, node):
        if node is None:
            return
        else:
            self._inorder(node.left)
            print node.value
            self._inorder(node.right)

    def _to_list(self, node, _list):
        if node is None:
            return
        else:
            self._to_list(node.left, _list)
            _list.append(node.value)
            self._to_list(node.right, _list)

    def to_list(self):
        _list = []
        self._to_list(self.root, _list)
        return _list

    def inorder(self):
        ''' Go left, visit the node and then go right. '''
        self._inorder(self.root)

    def _posorder(self, node):
        if node is None:
            return
        else:
            self._posorder(node.left)
            self._posorder(node.right)
            print node.value

    def posorder(self):
        ''' Go left, right and then visit the node '''
        self._posorder(self.root)

    def _height(self, node):
        if node is None:
            return 0
        else:
            left = self._height(node.left)
            right = self._height(node.right)
            return 1 + max(left, right) 

    def height(self):
        ''' Returns the height of the tree. A tree with only the root
        have height 0. '''
        return self._height(self.root) - 1

    def _search(self, node, key):
        if node.value == key:
            return True
        if node is None:
            return False
        else:
            if key < node.value:
                return self._search(node.left, key)
            else:
                return self._search(node.right, key)

    def search(self, key):
        ''' Searches for a key in the tree. O(log n) '''
        return self._search(self.root, key)

    def breadfs(self, start):
        queue = Queue.Queue()
        queue.put(start)
        while not queue.empty():
            adjacent = queue.get()
            print adjacent.value

            if adjacent.left is not None:
                queue.put(adjacent.left)
            if adjacent.right is not None:
                queue.put(adjacent.right)


if __name__ == "__main__":
    t = BinarySearchTree()

    # http://upload.wikimedia.org/wikipedia/commons/d/da/Binary_search_tree.svg
    values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    for val in values:
        t.insert(Node(val))

    t.insert(Node(1))

    print "Height: ", t.height()
    t.breadfs(t.root)
    
    # print t.preorder()
    # print t.inorder()
    # print t.posorder()







