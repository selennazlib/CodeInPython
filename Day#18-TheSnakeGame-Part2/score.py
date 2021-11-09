from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Arial", 20, 'normal')

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 250)
        self.score = 0

    def increase_score(self):
        self.score += 1
        self.clear()

    def show_score(self):
        self.write(f"Score {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)



