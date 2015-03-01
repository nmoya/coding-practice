#!/usr/bin/python
import Queue
import math
import sys


class Node():

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree():

    ''' This tree is unbalanced '''

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

    def _preorder(self, node):
        if node is None:
            return
        else:
            print node.value
            self._preorder(node.left)
            self._preorder(node.right)

    def preorder(self):
        ''' Visit the node, go left, and go right. Same as DFS.'''
        self._preorder(self.root)

    def _inorder(self, node):
        if node is None:
            return
        else:
            self._inorder(node.left)
            print node.value
            self._inorder(node.right)

    def inorder(self):
        ''' Go left, visit the node and then go right. Tree sort algorithm'''
        self._inorder(self.root)

    def _postorder(self, node):
        if node is None:
            return
        else:
            self._postorder(node.left)
            self._postorder(node.right)
            print node.value

    def postorder(self):
        ''' Go left, right and then visit the node. Useful for syntax trees
        berfore parsing the expression '''
        self._postorder(self.root)

    def _height(self, node):
        if node is None:
            return 0
        else:
            left = self._height(node.left)
            right = self._height(node.right)
            return 1 + max(left, right)

    def height(self, node=None):
        ''' Returns the height of the tree. A tree with only the root
        have height 0. '''
        if node is None:
            return self._height(self.root)
        else:
            return self._height(node)

    def _is_balanced(self, node):
        if node is None:
            return True
        else:
            left = self.height(node.left)
            right = self.height(node.right)
            return math.fabs(left - right) <= 1

    def is_balanced(self):
        return self._is_balanced(self.root)

    def _is_bst(self, node, _min, _max):
        if node is None:
            return True

        if node.value <= _min or node.value > _max:
            return False

        if not self._is_bst(node.left, _min, node.value) or \
                not self._is_bst(node.right, node.value, _max):
            return False
        return True

    def is_bst(self, node=None):
        if node is None:
            return self._is_bst(self.root, -sys.maxint, sys.maxint)
        else:
            return self._is_bst(node, -sys.maxint, sys.maxint)

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

    def largest_element(self, root):
        if root is not None:
            if root.right is None:
                return root.value
            else:
                return self.largest_element(root.right)

    def second_largest(self, root, parent):
        if root is not None:
            if root.right is None:
                if root.left is not None:
                    return self.largest_element(root.left)
                else:
                    return parent.value
            else:
                return self.second_largest(root.right, root)

    def _tree_level_to_list(self, node, levels_lists, level):
        if node is None:
            return
        else:
            self._tree_level_to_list(node.left, levels_lists, level + 1)
            levels_lists[level].append(node.value)
            self._tree_level_to_list(node.right, levels_lists, level + 1)

    def tree_level_to_list(self):
        height = self.height()
        levels_lists = [[] for i in range(height)]
        self._tree_level_to_list(self.root, levels_lists, 0)
        return levels_lists

    def is_child(self, node, key):
        if node is None:
            return False
        elif node.value == key:
            return True
        else:
            return self.is_child(node.left, key) or self.is_child(node.right, key)

    def first_common_ancestor(self, node, keyA, keyB):
        if node is None:
            return False
        
        if node.value == keyA or node.value == keyB:
            return node
        else:
            A_is_on_left = self.is_child(node.left, keyA)
            B_is_on_left = self.is_child(node.left, keyB)

            if (A_is_on_left != B_is_on_left):
                return node
            else:
                if A_is_on_left:
                    return self.first_common_ancestor(node.left, keyA, keyB)
                else:
                    return self.first_common_ancestor(node.right, keyA, keyB)


    def fst_common_ancestor(self, keyA, keyB):
        return self.first_common_ancestor(self.root, keyA, keyB).value


if __name__ == "__main__":
    t = BinarySearchTree()

    # http://upload.wikimedia.org/wikipedia/commons/d/da/Binary_search_tree.svg
    values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    for val in values:
        t.insert(Node(val))

    print "Height: ", t.height()
    # t.breadfs(t.root)

    print t.largest_element(t.root)
    print t.second_largest(t.root, None)

    print t.is_balanced()
    print t.is_bst(t.root)
    print t.tree_level_to_list()
    print t.is_child(t.root, 14)
    print t.fst_common_ancestor(7, 1)
    # print t.preorder()
    # print t.inorder()
    # print t.postorder()
