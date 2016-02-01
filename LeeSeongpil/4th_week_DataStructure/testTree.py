class TestTree:

    class Node:
        def __init__(self, element, left = None, right = None):
            self.element = element
            self.leftNode = left
            self.rightNode = right

    """ left와 right는 서브트리의 루트를 인자로 받는다."""
    def __init__(self, element, left = None, right = None):
        self.element = element
        self.leftSubTree = left
        self.rightSubTree = right
        self.mount = 1

    def __str__(self):
        return str(self.element)

    def makeRoot(self, e):
        new1 = self.Node(e)

    def addLeftSubTree(self, e):
        new1 = self.Node(e)
        self.leftSubTree = new1






