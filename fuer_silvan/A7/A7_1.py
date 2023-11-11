#!/usr/bin/env python3

#!/usr/bin/env python3

class MagicDrawingBoard:
    def __init__(self, x, y):
        if x <= 0 or y <= 0:
            raise Warning
        self.x = x
        self.y = y
        self.field = [[0 for i in range(x)] for j in range(y)]

    def pixel(self, coordinate):
        if coordinate[0] > self.x or coordinate[1] > self.y or coordinate[0] < 0 or coordinate[1] < 0:
            raise Warning
        else:
            self.field[coordinate[1]][coordinate[0]] = 1

    def rect(self, coordinate1, coordinate2):
        if coordinate1[0] > self.x or coordinate1[1] > self.y or coordinate1[0] < 0 or coordinate1[1] < 0:
            raise Warning
        elif coordinate2[0] > self.x or coordinate2[1] > self.y or coordinate2[0] < 0 or coordinate2[1] < 0:
            raise Warning
        elif coordinate1[0] > coordinate2[0] or coordinate1[1] > coordinate2[1]:
            raise Warning
        else:
            for i in range(coordinate1[1], coordinate2[1]):
                for j in range(coordinate1[0], coordinate2[0]):
                    self.field[i][j] = 1

    def img(self):
        string = ""
        for i in range(self.y):
            for j in range(self.x):
                string += str(self.field[i][j])
            string += "\n"
        return string[:-1]

    def reset(self):
        self.field = [[0 for i in range(self.x)] for j in range(self.y)]



db = MagicDrawingBoard(6, 4)  # instantiation of a specific size
db.pixel((1, 1))  # draw at one coordinate
db.rect((2, 2), (5, 4))  # draw a rectangle
img = db.img()  # return the drawn image
print(img)
db.reset()  # reset the field again
print(db.img())
db3 = MagicDrawingBoard(3, 3)  # instantiation of another specific size
db3.rect((1, 1), (3, 3))  # draw a rectangle
db3.rect((2, 2), (1, 1))  # draw a rectangle
