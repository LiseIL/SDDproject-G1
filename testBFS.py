#Created by isnel at 01/11/18

import unittest
from Graph import *
from copy import *

class testBFS(unittest.TestCase):

    def setUp(self):
        self.sommet0 = [0]
        self.sommet1 = [1]
        self.sommet2 = [2]
        self.sommet3 = [3]
        self.sommet4 = [4]
        self.sommet5 = [5]
        self.sommet6 = [6]
        self.sommet7 = [7]

        self.vertices0123 = self.sommet0 + self.sommet1 + self.sommet2 + self.sommet3
        self.vertices12 = self.sommet1 + self.sommet2
        self.vertices13 = self.sommet1 + self.sommet3
        self.vertices24 = self.sommet2 + self.sommet4
        self.vertices57 = self.sommet5 + self.sommet7
        self.vertices16 = self.sommet1 + self.sommet6

        self.vertices1257 = self.vertices12 + self.vertices57
        self.vertices1324 = self.vertices13 + self.vertices24
        self.vertices01257 = self.sommet0 + self.vertices1257

        self.successors1257 = [[2], [1, 5, 7], [2], [2]]
        self.successors1324 = [[2, 3], [1, 4], [1], [3]]
        self.successors0123 = [[1, 2], [0], [0, 3], [2]]
        self.successors01257 = [[1], [2], [1, 5, 7], [2], [2]]

        self.graph1257 = Graph(self.vertices1257, self.successors1257)
        self.graph1324 = Graph(self.vertices1324, self.successors1324)
        self.graph0123 = Graph(self.vertices0123, self.successors0123)
        self.graph01257 = Graph(self.vertices01257, self.successors01257)
        self.graphEmpty = Graph([],[])

    def testBFSEmpty(self):
        graph = copy(self.graphEmpty)
        res = graph.BFS([])
        expected = []
        self.assertEqual(res, expected)

    def testBFSgraph1257(self):
        graph = copy(self.graph1257)
        res = graph.BFS()
        expected = [2, 1, 5, 7]
        self.assertEqual(res, expected)

    def testBFSgraph1324(self):
        graph = copy(self.graph1257)
        res = graph.BFS()
        expected = [1, 2, 3, 4]
        self.assertEqual(res, expected)

    def testBFSgraph0123(self):
        graph = copy(self.graph0123)
        res = graph.BFS()
        expected = [0,1,2,3]
        self.assertEqual(res, expected)

    def testBFSgraph01257(self):
        graph = copy(self.graph01257)
        res = graph.BFS()
        expected = [0,1,2,5,7]
        self.assertEqual(res, expected)

