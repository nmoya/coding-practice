import unittest
import linkedlist
import stack
import queue
import queuewithstacks
import binarysearchtree
import random


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.list = linkedlist.List()

    def test_list_insert(self):
        for i in range(10):
            self.list.append(i)
        _list = self.list.to_list()
        self.assertEqual(_list, range(10))
        self.assertEqual(self.list.size, 10)

    def test_list_insert_ordered(self):
        tmp = []
        for i in range(100):
            r = random.randint(0, 100)
            self.list.insert_ordered(r)
            tmp.append(r)
        tmp.sort()
        _list = self.list.to_list()

        self.assertEqual(_list, tmp)
        self.assertEqual(tmp[0], self.list.first.value)
        self.assertEqual(tmp[-1], self.list.last.value)
        self.assertEqual(self.list.size, len(tmp))

    def test_list_reverse(self):
        tmp = []
        for i in range(100):
            r = random.randint(0, 100)
            self.list.insert_ordered(r)
            tmp.append(r)
        tmp.sort()
        tmp.reverse()
        initial_size = self.list.size
        self.list.reverse(self.list.first)
        _list = self.list.to_list()

        self.assertEqual(_list, tmp)
        self.assertEqual(tmp[0], self.list.first.value)
        self.assertEqual(tmp[-1], self.list.last.value)
        self.assertEqual(initial_size, self.list.size)

    def test_list_remove(self):
        for i in range(10):
            self.list.append(i)
        _list = self.list.to_list()
        elements = []
        elements.append(_list[0])
        elements.append(_list[int(len(_list) / 2)])
        elements.append(_list[-1])
        for el in elements:
            self.list.remove(el)
        _list = self.list.to_list()

        for el in elements:
            self.assertTrue(el not in _list)
        self.assertEqual(self.list.size, 10 - len(elements))

    def test_list_remove_duplicates(self):
        self.list.append(1)
        self.list.append(1)
        self.list.append(2)
        self.list.append(2)
        self.list.append(3)
        self.list.append(3)
        self.list.append(3)
        self.list.remove_duplicates()
        _list = self.list.to_list()
        self.assertEqual(_list, [1, 2, 3])
        self.assertEqual(self.list.size, 3)
        self.assertEqual(self.list.first.value, 1)
        self.assertEqual(self.list.last.value, 3)

    def test_list_practice(self):
        compare_list = []

        for i in range(1000):
            r = random.randint(-999, 999)
            self.list.insert_ordered(r)
            compare_list.append(r)
        tmp = compare_list[::]

        compare_list.sort()
        _list = self.list.to_list()
        self.assertEqual(_list, compare_list)
        self.assertEqual(compare_list[0], self.list.first.value)
        self.assertEqual(compare_list[-1], self.list.last.value)
        self.assertEqual(self.list.size, len(compare_list))

        for i in range(1000):
            r = random.randint(-999, 999)
            self.list.append(r)
            compare_list.append(r)
        _list = self.list.to_list()
        self.assertEqual(_list, compare_list)
        self.assertEqual(compare_list[0], self.list.first.value)
        self.assertEqual(compare_list[-1], self.list.last.value)
        self.assertEqual(self.list.size, len(compare_list))

        for i in range(500):
            if i % 2 == 0:
                element = random.choice(compare_list)
                compare_list.remove(element)
                self.list.remove(element)
            else:
                compare_list = compare_list[1:]
                self.list.remove_first()

        _list = self.list.to_list()
        self.assertEqual(_list, compare_list)
        self.assertEqual(compare_list[0], self.list.first.value)
        self.assertEqual(compare_list[-1], self.list.last.value)
        self.assertEqual(self.list.size, len(compare_list))


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = stack.Stack()

    def test_stack_push(self):
        tmp = []
        for i in range(30):
            r = random.randint(0, 100)
            self.stack.push(r)
            tmp.append(r)
        tmp.reverse()
        _list = self.stack.to_list()
        self.assertEqual(_list, tmp)
        self.assertEqual(self.stack.size, len(tmp))

    def test_stack_min(self):
        tmp = []
        for i in range(100):
            r = random.randint(0, 100)
            self.stack.push(r)
            tmp.append(r)
        tmp.reverse()
        _list = self.stack.to_list()
        self.assertEqual(self.stack.min(), min(tmp))

    def test_stack_remove(self):
        tmp = []
        for i in range(100):
            r = random.randint(0, 100)
            self.stack.push(r)
            tmp.append(r)
        tmp.reverse()
        for i in range(50):
            self.stack.pop()
        tmp = tmp[50:]
        _list = self.stack.to_list()
        self.assertEqual(_list, tmp)
        self.assertEqual(self.stack.min(), min(tmp))
        self.assertEqual(self.stack.size, len(tmp))

    def test_stack_push(self):
        tmp = []
        for i in range(100):
            r = random.randint(0, 100)
            self.stack.push(r)
            tmp.append(r)
        tmp.sort()
        tmp.reverse()
        self.stack.sort()
        _list = self.stack.to_list()
        self.assertEqual(_list, tmp)
        self.assertEqual(self.stack.size, len(tmp))


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = queue.Queue()

    def test_queue_enqueue(self):
        tmp = []
        for i in range(3):
            r = random.randint(0, 100)
            self.queue.enqueue(r)
            tmp.append(r)
        _list = self.queue.to_list()
        self.assertEqual(_list, tmp)
        self.assertEqual(self.queue.size, len(tmp))

    def test_queue_dequeue(self):
        tmp = []
        for i in range(100):
            r = random.randint(0, 100)
            self.queue.enqueue(r)
            tmp.append(r)
        for i in range(50):
            self.queue.dequeue()
        tmp = tmp[50:]
        _list = self.queue.to_list()
        self.assertEqual(_list, tmp)
        self.assertEqual(self.queue.size, len(tmp))


class TestQueueWithStacks(unittest.TestCase):

    def setUp(self):
        self.queue = queuewithstacks.QueueWithStacks()

    def test_queuestacks_enqueue(self):
        tmp = []
        for i in range(3):
            r = random.randint(0, 100)
            self.queue.enqueue(r)
            tmp.append(r)
        _list = self.queue.to_list()
        self.assertEqual(_list, tmp)
        self.assertEqual(self.queue.size, len(tmp))

    def test_queuestacks_dequeue(self):
        tmp = []
        for i in range(100):
            r = random.randint(0, 100)
            self.queue.enqueue(r)
            tmp.append(r)
        for i in range(50):
            self.queue.dequeue()
        tmp = tmp[50:]
        _list = self.queue.to_list()
        self.assertEqual(_list, tmp)
        self.assertEqual(self.queue.size, len(tmp))


class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.tree = binarysearchtree.BinarySearchTree()

    def test_tree_insert(self):
        values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
        for val in values:
            self.tree.insert(binarysearchtree.Node(val))
        _list = self.tree.to_list()
        values.sort()
        self.assertEqual(_list, values)

    def test_treeheight_dequeue(self):
        values = [3, 10, 1, 6, 14, 4, 7, 13]
        self.tree.insert(binarysearchtree.Node(8))
        self.assertEqual(self.tree.height(), 0)
        for val in values:
            self.tree.insert(binarysearchtree.Node(val))
        values.sort() 
        self.assertEqual(self.tree.height(), 3)

if __name__ == '__main__':
    unittest.main()
