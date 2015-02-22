import unittest
import linkedlist
import random


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.list = linkedlist.List()

    def test_insert(self):
        for i in range(10):
            self.list.insert(i)
        _list = self.list.to_list()
        self.assertEqual(_list, range(10))

    def test_insert_ordered(self):
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

    def test_reverse(self):
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

    def test_remove(self):
        for i in range(10):
            self.list.insert(i)
        _list = self.list.to_list()
        element = random.choice(_list)
        self.list.remove(element)
        _list = self.list.to_list()

        self.assertTrue(element not in _list)

    def test_remove_duplicates(self):
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


if __name__ == '__main__':
    unittest.main()
