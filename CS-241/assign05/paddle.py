import arcade
from point import Point

class Paddle:
    """
    Sets up the paddle params
    """
    def __init__(self):
        self.center = Point(x=390, y=(25, 275))

    def draw(self, width, height):
        """
        Draws the paddle on the screen
        """
        self.height = height
        arcade.draw_rectangle_filled(self.center.x, self.center.y, 
                                    width, height, arcade.color.BLACK)
        
    def move_up(self, move_amount, screen_height):
        """
        Tells the paddle to move up and stop at the top of the screen
        """
        if self.center.y < screen_height - self.height // 2:
            self.center.y += move_amount

    def move_down(self, move_amount):
        """
        Tells the paddle to move down and stop at the bottom of the screen
        """
        if self.center.y > 0 + self.height // 2:
            self.center.y -= move_amount
        