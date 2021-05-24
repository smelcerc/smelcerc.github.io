import arcade
from point import Point
from velocity import Velocity

class Ball:
    """
    This class handles the creation and managment for the pong ball
    """

    def __init__(self):
        self.center = Point(x=10, y=(10,290))
        self.velocity = Velocity()
        self.radius = 5
    
    def draw(self, ball_radius):
        self.radius = ball_radius
        arcade.draw_circle_filled(self.center.x, self.center.y, 
                                    self.radius, arcade.color.BLACK)

    def advance(self):
        self.height = 300
        self.width = 400
        self.direction_change = -1

        if self.center.x <= 0 + self.radius // 2:
            self.bounce_horizontal()

        if self.center.y >= self.height - self.radius // 2 or self.center.y <= 0 + self.radius // 2:
            self.bounce_vertical()

        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy 
            
    def bounce_horizontal(self):
        self.velocity.dx *= self.direction_change
        
    def bounce_vertical(self):
        self.velocity.dy *= self.direction_change
        

    def restart(self):
        self.__init__()