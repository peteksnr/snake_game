from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)  # we turned off the tracer method
game_is_on = True
snake = Snake()
food = Food()
score_board = ScoreBoard()
screen.listen()   # we are starting to listening events created by user
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with food.
    # we'll use the method distance
    # the distance method works by comparing the distance from this turtle to whatever it is that you put inside the ()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        print(score_board.track_score())
        # the write method first parameter arg is what it should write, align means what kind of alignment you want

    # detect collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset()

    # detect collision with the tail
    for segment in snake.snakes[1:]:
        # if segment == snake.head:
        #     pass
        # we've put the if statement because the first segment of the snake is its head our game wil be immediately over
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()


screen.exitonclick()
