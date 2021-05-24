import random

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = random.randint(y[0],y[1])

