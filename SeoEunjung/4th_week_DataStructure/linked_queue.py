class Empty(Exception):
    pass


class LlinkedQueue:

    class Node:

        def __init__(self, element, prev, next):
            # element : data /  prev, next : node
            self._element = element
            self._prev = prev
            self._next = next


    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        if self._size:
            return False
        else:
            return True

    # def add_first(self, e):
    #     if self._size == 0:
    #         new_node = self.Node(e, None, None)
    #         self._tail = new_node
    #     else:
    #         new_node = self.Node(e, None, self._head)
    #         self._head._prev = new_node
    #
    #     self._head = new_node
    #     self._size += 1

    def enqueue(self, e):
        new_node = self.Node(e, None, None)

        if self._size == 0:
            self._head = new_node
        else:
            new_node._prev = self._tail
            self._tail._next = new_node

        self._tail = new_node
        self._size += 1



    # 노드 반환? ㅇㅇ
    def dequeue(self):
        if self._size == 0:
            raise Empty("error")
        elif self._size == 1:
            result = self._head._element
            self._head, self._tail = None, None
            self._size = 0
            return result
        else:
            result = self._head._element
            self._head = self._head._next
            del self._head._prev
            self._head._prev = None
            self._size -= 1
            return result

    # # 노드 반환?
    # def remove_last(self):
    #     if self._size == 0:
    #         raise Empty("error")
    #     elif self._size == 1:
    #         self._head, self._tail = None, None
    #         self._size = 0
    #     else:
    #         self._tail = self._tail._prev
    #         del self._tail._next
    #         self._tail._next = None
    #         self._size -= 1


    # def insert(self, e):
    #     if self._size == 0:
    #         self.add_first(self, e)
    #     elif self._size == 1:
    #         self.add_last(self,e)



    def front(self):
        return self._head._element

    def end(self):
        return self._tail._element

    def print_list(self):
        if self._size == 0:
            print("None")
            return

        node = self._head
        element_list = list()
        while node._next:
            element_list.append(node._element)
            node = node._next
        else:
            element_list.append(self._tail._element)

        print(element_list)



class Tree:
    class Position:
        def element(self):
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            raise NotImplementedError('must be implemented by subclass')


    def root(self):
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height2(p)

    def __iter__(self):
        for p in self.positions():
            yield p.element()

    def positions(self):
        return self.preorder()

    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p


    def _subtree_postorder(self, p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def breadthfirst(self):
        if not self.is_empty():
            fringe = LlinkedQueue()
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                p = fringe.dequeue()
                yield p
                for c in self.children(p):
                    fringe.enqueue(c)