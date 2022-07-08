from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        #In order to appear circle very fast
        self.speed(0)
        """
        Since the size of the screen is 600x600 so according to turtle origin system the value of x originates from -300
        to +300 and same for the value of y i.e. [-300,300]. So we will place food under this coordinate system but
        there is a problem that there might be case when the random generated integer comes at -300 or +300 position
        which will be at the very edge of the screen and we can't see the food so we will generate random integers
        between -280 to +280.
        """
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
