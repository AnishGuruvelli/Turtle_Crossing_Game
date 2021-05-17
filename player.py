from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def go_up(self):
        # new_y = self.ycor() + MOVE_DISTANCE
        #
        # if new_y < FINISH_LINE_Y:
        #     self.goto(self.xcor(), new_y)
        # else:
        #     scoreboard.finish_line()

        # or just
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)
