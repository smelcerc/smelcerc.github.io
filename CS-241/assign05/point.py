import random

class Point:
    """
    Randomly sets the start location the ball and paddle
    """
    def __init__(self, x, y):
        #Sets the default start location for the ball and paddle on the x-axis
        self.x = x
        #Randomly sets the ball and paddle on the y-axis
        self.y = random.randint(y[0],y[1])

