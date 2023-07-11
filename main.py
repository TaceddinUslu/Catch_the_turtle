import turtle
import random #tur.hideturtle() kaplumbayı gizlemek için
from random import randint
drawing_board = turtle.Screen()
turtle_instance = turtle.Turtle()
score_instance = turtle.Turtle()
score = 0


def turtle_score():
    turtle.tracer(0)
    score_instance.hideturtle()

    score_instance.penup()
    score_instance.setposition(-50,290)

    score_instance.write("score: 0", move=True, font=("Arial", 15, "bold"))
    turtle.tracer(1)


def handle_click(x, y):
   global score
   score += 1
   score_instance.clear()
   score_instance.write("score: {}".format(score), move=True, font=("Arial", 15, "bold"))



turtle_instance.onclick(handle_click)

def turtle_turtle():
    drawing_board.bgcolor("white")
    turtle_instance.pencolor("light green")
    drawing_board.title("catch_the_turtle")
    turtle_instance.shape("turtle")
    turtle_instance.shapesize(1.4)


    turtle_instance.penup()
    turtle_instance.goto(randint(-300, 0), randint(0, 300))
    turtle_instance.speed(1)


    count = 0
    while count <50:
        count += 1
        if (turtle_instance.xcor() >-300 and turtle_instance.xcor() <300) and\
           (turtle_instance.ycor() >-300 and turtle_instance.ycor() <300):
            turtle_instance.forward(random.randint(30,100))
            turtle_instance.right(random.randint(0,180))
        else:
            turtle_instance.home()



















turtle_score()
turtle_turtle()
handle_click()






turtle.mainloop()
