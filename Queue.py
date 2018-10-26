################
# Python 3.5 File
# Group 1
# created oct. 24th 2018
# last modif oct. 24th 2018
# Queue.py
################

#Une file est une liste où les insertions se font d'un
#côté et les suppressions se font de l'autre côté

#[Lise]
#1- Est-ce qu'on est sûre que les valeurs stockées dans notre queue
# doivent obligatoirement être de type Int ? Pourquoi pas des Float ? ou Str ?

#2- J'ai un petit soucis avec les types des méthodes.
# Par exemple, pour getList() j'aurais indiqué:
#   """Queue -> List"""
# Est-ce que tu es d'accord ?

#3-Pour dequeue, est-ce qu'on autorise l'application de la méthode à une file vide ?

class Queue :

    def __init__(self, list):
        """ The empty queue is the queue with [] argument """
        #assert isinstance(list, list)
        self.list = list

    def getList(self):
        """ None --> list """
        return self.list

    def setList(self, value):
        """ List --> None """
        assert isinstance(value, list) #[Lise] j'aurais mis cette ligne de vérification
                                       #        dans la constructeur __init__ qu'en penses-tu ?
        self.list = value

    def isEmpty(self):
        """ None --> Bool """
        if (self.getList() == []):
            return True
        else:
            return False

    def enqueue(self, value):
        """ Int --> None
        ----------------
        Add the value at the end (right side) of the queue """
        assert isinstance(value, int)
        list = self.getList()
        list = list + [value]
        self.setList(list)

    def dequeue(self):
        """ Queue --> None
         ----------------
        If the queue is not empty, removes the value at the beginning (left side) of the queue
        Else, nothing"""
        if not self.isEmpty():
            queue = self.getList()
            newQueue = queue[1:]
            self.setList(newQueue)

    def peek(self):
        """Queue -> Int
        ---------------
        Peek the first element (on the left-hand side of the queue)"""
        assert(not self.isEmpty())
        list = self.getList()
        return list[0]

