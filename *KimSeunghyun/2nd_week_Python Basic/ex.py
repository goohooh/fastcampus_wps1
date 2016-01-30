class C(object):
    def __init__(self, v):
        self.value = v
    def show(self):
        print(self.value)

c1 = c(10)
print(c1.value)