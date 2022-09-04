# import Turtle and Screen classes
from turtle import Turtle, Screen
import random
# create a boolean variable to check if the while loop is still active.
is_race_on = False
# create creen instance
screen = Screen()
#set screen
screen.setup(width=500, height=400)
# take in user input of who would win.
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? enter a color")
#colors list
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
#positions of turtles starting point on the screen grid
y_positions = [-70, -40, -10, 20, 50, 80]
#empty list to insert the turtles
all_turtles = []
#create the turtle instances and append them to the turtles list.
for index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[index])
    all_turtles.append(new_turtle)

# check if the user bet is taken.
if user_bet:
    is_race_on = True
# loop through the turtle instances and check that they move, and do not pass the thresh hold.
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} turtle is the winner")
            else:
                print(f"You've lost! the {winning_color} turtle is the winner")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()