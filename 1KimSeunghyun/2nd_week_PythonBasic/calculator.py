class CalMultiply():
    def multiply(self):
        result = self.v1*self.v2
        Cal._history.append("multiply : %d*%d=%d" % (self.v1, self.v2, result))
        return result
    def info(self):
        return "CalMultiply => %s" % super().info()

class CalDivide():
    def divide(self):
        result = self.v1/self.v2
        Cal._history.append("divide : %d/%d=%d" % (self.v1, self.v2, result))
        return result
    def info(self):
        return "CalDivide => %s" % super().info()

class Cal(CalMultiply, CalDivide):
    _history = []
    def __init__(self, v1, v2):
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2
    def add(self):
        result = self.v1+self.v2
        Cal._history.append("add : %d+%d=%d" % (self.v1, self.v2, result))
        return result
    def subtract(self):
        result = self.v1-self.v2
        Cal._history.append("subtract : %d-%d=%d" % (self.v1, self.v2, result))
        return result
    # def setV1(self, v):
    #     if isinstance(v, int):
    #         self.v1 = v
    #     else:
    #         print("error")
    # def getV1(self):
    #     return self.v1

    @classmethod
    def history(cls):
        for item in Cal._history:
            print(item)

    def info(self):
        return "Cal => v1 : %d, v2 : %d" % (self.v1, self.v2)


c = Cal(100, 10)
print(c.add())
print(c.multiply())
print(c.divide())