import random

class Velocity:
    """
    Randomly set the speed and direction of the ball
    """
    def __init__(self):
        #Only allow the ball to move forward
        self.dx = random.randint(1,5)
        #Allows the ball to start off going up or down
        self.dy = random.randint(-5,5)
