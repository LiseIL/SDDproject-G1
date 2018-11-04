__author__ = "Group 1"
__filename__ = "tests_queue"
__creationdate__ = "29/10/18"

import unittest
from copy import *
from queue import *


class QueueTest(unittest.TestCase):
    def setUp(self):
        self.emptyQueue = Queue([])
        self.queue1 = Queue([1])
        self.queue123 = Queue([1,2,3])
        self.queue23 = Queue([2,3])

    def testGetEmptyList(self):
        queue = copy(self.emptyQueue)
        value = queue.getList()
        expected = []
        self.assertTrue(value == expected)

    def testGetList(self):
        queue = copy(self.queue1)
        value = queue.getList()
        expected = [1]
        self.assertTrue(value == expected)

    def testSetList(self):
        queue = copy(self.queue1)
        queue.setList([1, 2, 3])
        value = queue.getList()
        expected = [1, 2, 3]
        self.assertTrue(value == expected)

    def testSetListError(self):
        queue = copy(self.queue1)
        try:
            value = queue.setList((1, 2, 3))
        except:
            self.assertRaises(AssertionError)

    def testIsNotEmpty(self):
        queue = copy(self.queue1)
        value = queue.isEmpty()
        expected = False
        self.assertTrue(value == expected)

    def testIsEmpty(self):
        queue = copy(self.emptyQueue)
        value = queue.isEmpty()
        expected = True
        self.assertTrue(value == expected)

    def testEnqueue(self):
        queue = copy(self.emptyQueue)
        queue.enqueue(2)
        value = queue.getList()
        expected = [2]
        self.assertTrue(value == expected)

    def testEnqueueError(self):
        queue = copy(self.queue1)
        try:
            value = queue.enqueue('a')
        except:
            self.assertRaises(AssertionError)

    def testPeekEmpty(self):
        queue = copy(self.emptyQueue)
        try:
            value = queue.peek()
        except:
            self.assertRaises(AssertionError)

    def testPeek(self):
        queue = copy(self.queue1)
        print(queue)
        value = queue.peek()
        print(value)
        expected = 1
        print(expected)
        self.assertTrue(value == expected)

    def testPeek123(self):
        queue = copy(self.queue123)
        value = queue.peek()
        expected = 1
        self.assertTrue(value == expected)

    def testDequeueEmpty(self):
        queue = copy(self.emptyQueue)
        try:
            value = queue.dequeue()
        except:
            self.assertRaises(AssertionError)

    def testDequeue(self):
        queue = copy(self.queue1)
        queue.dequeue()
        expected = copy(self.emptyQueue)
        self.assertEqual(queue.getList(), expected.getList())


    def testDequeue123(self):
        queue = copy(self.queue123)
        queue.dequeue()
        expected = copy(self.queue23)
        self.assertEqual(queue.getList(),expected.getList())
