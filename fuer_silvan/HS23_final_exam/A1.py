
class Data:
    def __init__(self, dat):
        self.data = dat

    def compute(self, f1, f2):
        return f1(self.data), f2(self.data)






objects = [1.7, 2.3, 3, 4]
d = Data(objects)
print( d.data is objects )
print( d.compute(sum, min) )
print( d.compute(min, max) )