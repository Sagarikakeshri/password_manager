
import random
import turtle
is_race_on=False
screen=turtle.Screen()
screen.setup(width=500,height=400)
user=screen.textinput(title="Make your bet",prompt="Which Turtle will win the race? Enter a color: ")
colors=["red","orange","yellow","blue","green","purple"]
y_positions=[-70,-40,-10,20,50,80]
all_turtle=[]
for i in range(0,6):
    new_turtle=turtle.Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[i])
    new_turtle.color(colors[i])
    all_turtle.append(new_turtle)
if user:
    is_race_on=True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user:
                print("you won")
        random_distance=random.randint(0,10)
        turtle.forward(random_distance)




screen.exitonclick()