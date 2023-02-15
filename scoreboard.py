from turtle import Turtle
FONT = ("Times", 18, "normal")
ALIGNMENT = 'center'
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.goto(-20,275)
        self.update_score()


    def update_score(self):
        self.write(f"Score: {self.score}", font=FONT,align=ALIGNMENT)


    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", font=FONT,align=ALIGNMENT)

    def score_increase(self):
        self.score += 1
        self.clear()
        self.update_score()