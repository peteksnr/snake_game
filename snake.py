from turtle import Turtle
STARTING_POSITIONS = [(20, 0), (0, 0), (-20, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snakes()
        self.head = self.snakes[0]

    def create_snakes(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        # add a new segment to the snake
        new_snake = Turtle(shape='square')
        new_snake.color('white')
        new_snake.penup()
        new_snake.goto(position)
        self.snakes.append(new_snake)

    def extend(self):
        self.add_segment(self.snakes[-1].position())  

    def move(self):
        for seg_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[seg_num - 1].xcor()
            new_y = self.snakes[seg_num - 1].ycor()
            self.snakes[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.snakes:
            seg.goto(1000, 1000)
        self.snakes.clear()
        self.create_snakes()
        self.head = self.snakes[0]

    def up(self):
        if self.head.heading() != DOWN: 
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP: 
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
