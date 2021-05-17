# Turtle_Crossing_Game
Turtle crossing the finish line and level increases

Steps:

*** Steps to be followed while making the turtle crossing game ***

1. create a turtle body
2. move the turtle, only with the up key (It can only move forwards, not back, left or right.)
3. Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.
4. detect collision with the cars (When the turtle collides with a car, it's game over and everything stops.)
5. create a scoreboard
6. When the turtle hits the top edge of the screen, it moves back to the original position and the player levels up.
On the next level, the car speed increases.

car = [length = 20, width = 40]
No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for our little turtle).
