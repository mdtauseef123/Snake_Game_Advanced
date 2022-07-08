from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
#To turn off the animation we use tracer() and 0 is used when we have to off the animation
screen.tracer(0)
snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()
"""
For upper arrow key "Up" is used in key arguments in the same case no change.
Similarly, "Down","Left","Right" is used for down,left and right arrow keys.
"""
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)

game_is_on = True
while game_is_on:
    #Tells the compiler to redraw the new drawing/movements only after it completes the one move i.e. move forwarded
    #screen.update() is used when tracer is turned off
    screen.update()
    #Once the new movement is shown on the screen then we can wait for a certain specific time for the new drawing
    #or movement in seconds. 0.1 is fastest
    time.sleep(0.1)
    snake.move_snake()
    #Detect collision with food
    """
    In order to detect collision with food we will just use distance() which used to find the distance between the two
    turtle object so we just take the head i.e. very first segment and compare with the food object turtle and if the 
    distance comes out to be less than 15 then we say that the head of the snake collided with the food object. We use 
    15 because size of the snake is 10x10 and if the distance comes out to be say 15 then we will assume that head is
    collided with the snake. We can give value according to our need. The greater we value put in the more easily the 
    collision will happen. It all depends on accuracy if we want the head on collision we can give 10 or if we are happy
    just passing after the food then we can give big number.
    """
    if snake.head.distance(food) < 15:
        snake.extend()
        score.update_score()
        food.refresh()

    #Detect collision with wall
    """
    Now we don't want our game to be over when the game when the snake collides with the wall or tit's tail instead 
    what we want to update the high score and restart the game.
    """
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_score_board()
        #Not just we want to reset the score board but also reset the snake i.e. to start the snake at the initial
        #position where we started earlier and to remove the previous snake from the user screen i.e. 600x600
        snake.reset_snake()
        #game_is_on = False
        #score.game_over()

    #Detect collision with tail or body
    for segment in snake.segments:
        #If the distance between the head and any of the segment is less than 10 then collision happens
        #But there is problem in line no 64 as we are looping all segments then the very first segment is itself is head
        #So when we check if snake.head.distance(segment) < 10 it will satisfy this condition and the game will
        #terminate without even hitting the body of the snake In order to avoid these we used line number 62 so in every
        #first case it will just skip the loop OR we can just use the concept of slicing i.e. in the below line
        #for segment in snake.segments[1:]: that it will skip the first segment(head) and hence we can skip line 62 & 63
        if segment == snake.head:
            continue
        if snake.head.distance(segment) < 10:
            score.reset_score_board()
            snake.reset_snake()
            #game_is_on = False
            #score.game_over()

screen.exitonclick()
