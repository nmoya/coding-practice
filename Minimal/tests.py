import unittest
import linkedlist
import stack
import random


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.list = linkedlist.List()

    def test_list_insert(self):
        for i in range(10):
            self.list.insert(i)
        _list = self.list.to_list()
        self.assertEqual(_list, range(10))

    def test_list_insert_ordered(self):
        tmp = []
        for i in range(100):
            r = random.randint(0, 100)
            self.list.insert_ordered(r)
            tmp.append(r)
        tmp.sort()
        _list = self.list.to_list()
        self.assertEqual(_list, tmp)
        self.assertEqual(_list[0], self.list.first.value)
        self.assertEqual(_list[-1], self.list.last.value)

    def test_list_reverse(self):
        tmp = []
        for i in range(100):
            r = random.randint(0, 100)
            self.list.insert_ordered(r)
            tmp.append(r)
        tmp.sort()
        tmp.reverse()
        self.list.reverse(self.list.first)
        _list = self.list.to_list()
        self.assertEqual(_list, tmp)
        self.assertEqual(_list[0], self.list.first.value)
        self.assertEqual(_list[-1], self.list.last.value)

    def test_list_remove(self):
        for i in range(10):
            self.list.insert(i)
        _list = self.list.to_list()
        elements = []
        elements.append(_list[0])
        elements.append(_list[int(len(_list)/2)])
        elements.append(_list[-1])
        for el in elements:
            self.list.remove(el)
        _list = self.list.to_list()
        for el in elements:
            self.assertTrue(el not in _list)

    def test_list_remove_duplicates(self):
        self.list.insert(1)
        self.list.insert(1)
        self.list.insert(2)
        self.list.insert(2)
        self.list.insert(3)
        self.list.insert(3)
        self.list.insert(3)
        self.list.remove_duplicates()
        _list = self.list.to_list()
        self.assertEqual(_list, [1, 2, 3])


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = stack.Stack()

    def test_stack_push(self):
        tmp = []
        for i in range(3):
            r = random.randint(0, 100)
            self.stack.push(r)
            tmp.append(r)
        tmp.reverse()
        _list = self.stack.to_list()
        self.assertEqual(_list, tmp)
        self.assertEqual(len(_list), len(tmp))

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

if __name__ == '__main__':
    unittest.main()
