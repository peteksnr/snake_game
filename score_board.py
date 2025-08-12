from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def get_high_score(self):
        with open("data.txt", 'r') as file:
            high_score = int(file.read())
            return high_score

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}   High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", 'w') as file:
                file.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def track_score(self):
        self.score += 1
        self.update_scoreboard()
