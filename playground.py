import turtle


def draw_circle():

    my_circle = turtle.Turtle()
    my_circle.shape("circle")
    my_circle.circle(75)
    my_circle.color("white")


def draw_square():

    my_square = turtle.Turtle()
    my_square.shape("turtle")
    my_square.color("#000000")
    my_square.speed(2)

    turn = [1 ,2, 3, 4]

    for i in turn:
        my_square.forward(100)
        my_square.right(90)


def draw_shapes():

    window = turtle.Screen()
    window.bgcolor("#80CDFF")

    draw_square()
    draw_circle()

    window.exitonclick()


draw_shapes()