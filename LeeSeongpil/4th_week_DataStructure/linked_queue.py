class LinkedQueue:
    class Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        if self.__len__() == 0:
            return True
        else:
            return False

    # def add_first(self, el):
    #     new1 = self.Node(el, next)
    #
    #     if self._size == 0:
    #         new1._next = None
    #         self._head = new1
    #         self._tail = new1
    #         # self._temp = new1
    #         self._size += 1
    #     else:
    #         new1._next = self._head
    #         self._head = new1
    #         self._size += 1

    def enqueue(self, el):
        new1 = self.Node(el, None)

        if self._size == 0:
            self._head = new1
            self._tail = new1
            self._size += 1
        else:
            self._tail._next = new1
            self._tail = new1
            self._size += 1

    def dequeue(self):
        if self._size == 0:
            print('the list is empty')
        else:
            a = self._head
            self._head = self._head._next
            a._next = None
            self._size -= 1
            return a._element

    # def remove_last(self):
    #     if self._size == 0:
    #         print('the list is empty')
    #     else:
    #         a = self._head
    #         while a._next != self._tail:
    #             a = a._next
    #         self._tail = a
    #         a._next = None
    #         self._size -= 1

    def front(self):
        return self._head._element

    def back(self):
        return self._tail._element

    def print_list(self):
        if self._size == 0:
            print('the list is empty')
        else:
            a = self._head
            while a != self._tail:
                print(a._element, '<-', end=' ' )
                a = a._next
            print(a._element)

tree = LinkedQueue()

tree.enqueue(2)
tree.print_list()
tree.enqueue(9)
tree.print_list()
tree.enqueue(7)
tree.print_list()
print(tree.front())
print(tree.dequeue())
tree.print_list()
print(tree.front())
print(tree.back())