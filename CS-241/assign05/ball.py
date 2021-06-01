import arcade
from point import Point
from velocity import Velocity

class Ball:
    """
    This class handles the creation and managment for the pong ball
    """

    def __init__(self):
        """
        Sets the init state of the ball
        """
        self.center = Point(x=10, y=(10,290))
        self.velocity = Velocity()
        self.radius = 5
    
    def draw(self, ball_radius):
        """
        Draws the ball on the display
        """
        self.radius = ball_radius
        arcade.draw_circle_filled(self.center.x, self.center.y, 
                                    self.radius, arcade.color.BLACK)

    def advance(self):
        """
        Moves the ball in a direction depending on if it bounced off a wall or not
        """
        self.height = 300
        self.width = 400
        self.direction_change = -1

        #Only checks if the ball bounces off the left wall. Theres a method on in Pong.py that bounces off the paddle
        if self.center.x <= 0 + self.radius // 2:
            self.bounce_horizontal()

        #Bounces off the top and bottom of the screen
        if self.center.y >= self.height - self.radius // 2 or self.center.y <= 0 + self.radius // 2:
            self.bounce_vertical()

        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy 
            
    def bounce_horizontal(self):
        """
        Keeps the ball between the left and right sides of the screen
        """
        self.velocity.dx *= self.direction_change
        
    def bounce_vertical(self):
        """
        Keeps the ball between the top and bottom of the screen
        """
        self.velocity.dy *= self.direction_change
        

    def restart(self):
        """
        Restarts the ball if the ball goes passed the paddle
        """
        self.__init__()