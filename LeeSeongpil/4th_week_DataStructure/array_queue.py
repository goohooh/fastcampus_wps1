class Empty(Exception):
    pass

class ArrayQueue:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        if self.__len__() == 0:
            return True
        else:
            return False

    def first(self):
        if self.is_empty() == True :
            print('Empty list')
        else:
            return self._data[0]

    def dequeue(self):
        if self.is_empty() == True:
            print('Error')
        else:
            returnData = self._data[0]
            self._data = self._data[1:]
            return returnData

    def enqueue(self, e):
        self._data.append(e)

s = ArrayQueue()


print(s._data)