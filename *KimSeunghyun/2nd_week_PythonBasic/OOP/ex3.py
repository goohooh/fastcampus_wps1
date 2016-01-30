class Cs:
    @staticmethod
    def sm():
        print("Static method")
    @classmethod
    def cm(cls ):
        print("Class method")
    def instance_method(self):
        print("Instance method")


i = Cs()
Cs.sm()
Cs.cm()
i.instance_method()