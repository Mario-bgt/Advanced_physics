#!/usr/bin/env python3

class MagicDrawingBoard:
    def __init__(self, x, y):
        if x <= 0 or y <= 0:
            raise Warning("The size of the drawing board must be positive.")
        self.x = x
        self.y = y
        self.field = [[0 for i in range(x)] for j in range(y)]

    def pixel(self, coordinate):
        if coordinate[0] > self.x or coordinate[1] > self.y or coordinate[0] < 0 or coordinate[1] < 0:
            raise Warning("Pixel outside of the created board")
        else:
            self.field[coordinate[0]][coordinate[1]] = 1

    def rect(self, coordinate1, coordinate2):
        if coordinate1[0] > self.x or coordinate1[1] > self.y or coordinate1[0] < 0 or coordinate1[1] < 0:
            raise Warning("Coordinates out of bounds")
        elif coordinate2[0] > self.x or coordinate2[1] > self.y or coordinate2[0] < 0 or coordinate2[1] < 0:
            raise Warning("Coordinates out of bounds")
        elif coordinate1[0] > coordinate2[0] or coordinate1[1] > coordinate2[1]:
            raise Warning('The rectangle must be "positive", i.e., the end coordinates must be to the lower right '
                             'of the start coordinates.')
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
