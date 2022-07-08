from turtle import Turtle
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segments = Turtle()
        new_segments.color("white")
        new_segments.shape("square")
        # Before going to goto() and moving forward we don't want the way line to show up on the screen,so we
        # execute penup()
        new_segments.penup()
        new_segments.goto(position)
        self.segments.append(new_segments)

    def reset_snake(self):
        #Sending all the snake beyond the screen of view i.e. 600x600
        for seg in self.segments:
            seg.goto(1000, 1000)
        #It will empty the segments list using clear()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    #To extend the snake everytime when the snake eats the food
    #position() return the turtle’s current location (x,y)
    #So we will take the position of last added segment, and then we will add new segment at the end of it
    #In the very first case the position() will return (-60,0) so the new segment will be added at (-60,0) position.
    #Hence the very last segment is at the position (-80,0)
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move_snake(self):
        """
            In order to move the snake we will move from last segments to first segments each by each i.e. third segment
             is move to the position of second segment and second segment is moved towards the position of first
            segments and at last we will just change the movement of first position according to our choice in which
            direction we want to move the snake.This algorithm will work for any kind of movement i.e. left,right,up
            and down.
        """
        for seg_ind in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_ind - 1].xcor()
            new_y = self.segments[seg_ind - 1].ycor()
            self.segments[seg_ind].goto(new_x, new_y)
        self.head.forward(20)

    """
    We know the rule of the game i.e. when the snake is moving in the left direction then instantly it cannot move in 
    the right direction for this the snake have to move in the up/down direction and then it can turn right.
    Similarly rules are applied for moving,up and right direction.Due to this reason we have given the if statement in
    every movement before we make any kind of movement.
    """

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
