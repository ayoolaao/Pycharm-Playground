import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    ayo = turtle.Turtle()
    ayo.forward(100)
    ayo.right(90)

    window.exitonclick()

draw_square()