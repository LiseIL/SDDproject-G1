__author__ = "Group 1"
__filename__ = "graph"
__creationdate__ = "29/10/18"

from queue import *


class Graph:
    def __init__(self, vertices, successors):
        assert isinstance(vertices, list)
        assert isinstance(successors, list)
        assert (len(vertices) == len(successors))
        for i in range(len(vertices)):
            x = vertices[i]  # i-th vertex
            assert isinstance(successors[i], list)
            for j in range(len(successors[i])):
                y = successors[i][j]  # j-th successor of x
                ind = vertices.index(y)  # index of y in vertices
                assert x in successors[ind]  # x in successor of y

        self.vertices = vertices
        self.successors = successors

    def getVertices(self):
        """ None --> list """
        return self.vertices

    def getSuccessors(self):
        """ None --> list """
        return self.successors

    def setVertices(self, vertices):
        """ list --> None """
        assert isinstance(vertices, list)
        self.vertices = vertices

    def setSuccessors(self, successors):
        """ list --> None """
        assert isinstance(successors, list)
        self.successors = successors


    def BreadthFirstSearch(self, vertex0, marks):
        """ (graph, int, list) --> list
        list of vertices in breadth order"""
        assert isinstance(vertex0, int)
        assert isinstance(marks, list)

        queue = Queue([])
        queue.enqueue(vertex0)
        Vertices = []
        successors = self.getSuccessors()
        vertices = self.getVertices()
        while not queue.isEmpty():
            vertex = queue.peek()
            queue.dequeue()
            if not marks[vertex]:
                marks[vertex] = True
                Vertices += [vertex]
                #successors = self.getSuccessors()
                for i in range(len(successors[vertex])):
                    queue.enqueue(successors[vertex][i])

        #For the case where  the graph is not related:
        successorsNotRelated = []
        verticesNotRelated = []
        marksNotRelated = []
        for i in range (len(marks)):
            if marks[i] == False:
                verticesNotRelated += vertices[i]
                successorsNotRelated += successors[i]
                marksNotRelated += [False]
        if not(verticesNotRelated == []):
            graphBis = Graph(verticesNotRelated, successorsNotRelated)
            verticesbis = graphBis.BreadthFirstSearch(verticesNotRelated[0], marksNotRelated)
            Vertices += [verticesbis]

        return Vertices
