from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial",22,"normal")

class ScoreBoard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-20,270)
        self.color("white")
        self.score = -1
        self.high_score = self.load_HS()
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_HS()
        self.score = -1
        self.update_score()

    def load_HS(self):
        hi = 0
        with open("hs.txt") as file:
            hi = file.read()
        return int(hi)
    
    def save_HS(self):
        with open("hs.txt", "w") as file:
            file.write(str(self.high_score))
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
