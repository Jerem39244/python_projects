import turtle

screen = turtle.Screen()
my_turtle = turtle.Turtle()

for _ in range(3):
    my_turtle.forward(100)
    my_turtle.left(120)
my_turtle.penup()
my_turtle.left(180)
my_turtle.forward(30)
my_turtle.pendown()
for _ in range(6):
    my_turtle.forward(100)
    my_turtle.left(60)
my_turtle.penup()
my_turtle.right(90)
my_turtle.forward(30)
my_turtle.pendown()
for _ in range(2):
    my_turtle.forward(30)
    my_turtle.left(90)
    my_turtle.forward(60)
    my_turtle.left(90)

turtle.done()