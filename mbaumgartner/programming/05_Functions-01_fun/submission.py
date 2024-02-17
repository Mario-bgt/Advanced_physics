class Data:
    def __init__(self, dat):
        self.data = dat

    def compute(self, f1, f2):
        return f1(self.data), f2(self.data)
        