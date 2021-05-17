from turtle import Turtle

FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.color("Blue")
        self.penup()
        self.hideturtle()
        self.player_level = 1
        self.goto(-250, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"LEVEL: {self.player_level}", font=FONT)

    def increase_level(self):
        self.player_level += 1
        self.update_scoreboard()

    def game_over(self):
        # self.goto(    -90, 0)  # or we can also keep alignment as center
        self.goto(0, 0)
        self.write("GAME OVER !!", align="center", font=FONT)

