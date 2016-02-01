class LinkedList:
    class Node:
        def __init__(self, element, prev = None, next = None): #prev, next 키워드 인자
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
        if self.__len__() == 0:
            return True
        else:
            return False

    def add_first(self, el):
        new1 = self.Node(el)

        if self._size == 0:
            new1._next = None
            new1._prev = None
            self._head = new1
            self._tail = new1
            self._size += 1
        else:
            new1._next = self._head
            self._head._prev = new1
            new1._prev = None
            self._head = new1
            self._size += 1

    def add_last(self, el):
        new1 = self.Node(el)

        if self._size == 0:
            new1._next = None
            new1._prev = None
            self._head = new1
            self._tail = new1
            self._size += 1
        else:
            self._tail._next = new1
            new1._prev = self._tail
            self._tail = new1
            self._size += 1

    def remove_first(self):
        if self._size == 0:
            print('the list is empty')
        else:
            self._head = self._head._next
            self._head._prev = None
            self._size -= 1

    def remove_last(self):
        if self._size == 0:
            print('the list is empty')
        else:
            self._tail = self._tail._prev
            self._tail._next = None
            self._size -= 1

    """현재 엘리먼트(now_el) 뒤에 새로운 엘리먼트(e)를 넣는다."""
    def insert(self, now_el, e):
        new1 = self.Node(e)

        if self._size == 0:
            self.add_first(e)
        elif self._size == 1:
            self.add_last(e)
        else:
            temp = self._head #현재 포커싱 노드를 담을 temp 객체 생성

            """temp의 next가 지정한 엘레먼트와 동일할 때까지 반복"""
            while temp._element != now_el:
                temp = temp._next
            """현재 노드를 A, A의 next B, 새로 생성되어 A와 B 사이에 삽입할 노드 C라 칭함"""
            new1._prev = temp               # C의 prev로 A 지정
            new1._next = temp._next         # 원래 A의 next였던 B를 C의 next로 지정
            temp._next = new1               # A의 next로 C를 바라보도록 함
            temp._next._next._prev = new1   # A의 next(C)의 next(B)의 prev를 C로 지정

    def remove(self, el):
        if self._size == 0:
            print('empty list')
        elif self._size == 1 and self._head._element == el:
            self._head = None
            self._tail = None
        elif self._size >= 2:
            if self._head._element == el:
                self.remove_first()
            elif self._tail._element == el:
                self.remove_last()
            else:
                pass
            temp = self._head
            while temp._element != el:
                temp = temp._next
            front = temp._prev
            back = temp._next
            front._next = back
            back._prev._next = None
            back._prev._prev = None
            back._prev = front
        else:
            print('Error: wrong argument input')



    def head(self):
        return self._head._element

    def tail(self):
        return self._tail._element

    def print_list(self):
        if self._size == 0:
            print('the list is empty')
        else:
            a = self._head
            while a != self._tail:
                print(a._element, '->', end=' ' )
                a = a._next
            print(a._element)


lst = LinkedList()
print(lst.is_empty()) #True
lst.add_first(1)  #1
print(lst.tail()) #return 1

print(lst.head()) #return 1
lst.add_first(2)  #2->1
lst.add_first(3)  #3->2->1
lst.print_list()  #2->1->4->5

print(lst.tail()) #return 1
lst.add_last(4)  #3->2->1->4
lst.add_last(5)  #3->2->1->4->5
lst.print_list()  #2->1->4->5

lst.add_last(6)  #3->2->1->4->5->6
lst.remove_first()  #2->1->4->5->6
lst.remove_last()  #2->1->4->5
lst.print_list()  #2->1->4->5
print(lst.is_empty()) #False
len(lst)  #return 4
print('===================')
lst.remove(1) #2->4->5
lst.print_list()
lst.insert(2,8) #2->8->4->5
lst.print_list()
lst.remove_first() #8->4->5
lst.print_list()