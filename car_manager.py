from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()

        self.all_cars = []
        self.carspeed = STARTING_MOVE_DISTANCE

    # def create_car(self):
    #     new_Car = Turtle("square")
    #     # all turtle start by 20 by 20 and this needs to be 20 by 100 so we need to stretch it
    #     new_Car.shapesize(stretch_len=2, stretch_wid=1)
    #     new_Car.penup()
    #     new_Car.hideturtle()
    #     new_Car.color(random.choice(COLORS))
    #     random_y = random.randint(-250, 250)
    #     new_Car.goto(300, random_y)
    #     self.all_cars.append(new_Car)
    """the error with the above code is that there are a bit oo many cars which are generated so in the below code
    we are going to make it in such a way that, a car is generated every 1 in 6 times like how a dice is rolled
    and we can make sure that a car if formed when it shows 1 on the diec or any other number"""

    def create_car(self):
        # now this basically shows that every 6 times the while loop in the main function runs a car will be generated
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            # all turtle start by 20 by 20 and this needs to be 20 by 100 so we need to stretch it
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-200, 200)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.carspeed)

    def level_up(self):
        self.carspeed += MOVE_INCREMENT
