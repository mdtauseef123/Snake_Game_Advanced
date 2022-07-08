from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        file = open("data.txt", mode="r")
        self.high_score = int(file.read())
        file.close()
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.color("white")
        self.message()

    def update_score(self):
        self.score += 1
        self.message()

    def message(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score_board(self):
        if self.score > self.high_score:
            self.high_score = self.score
            file = open("data.txt", mode="w")
            file.write(str(self.high_score))
            file.close()
        self.score = 0
        self.message()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
