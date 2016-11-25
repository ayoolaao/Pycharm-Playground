import turtle


def draw_circle():

    my_circle = turtle.Turtle()
    my_circle.shape("circle")
    my_circle.circle(75)
    my_circle.color("#46FF18")


def draw_square():

    my_square = turtle.Turtle()
    my_square.shape("arrow")
    my_square.color("red")
    my_square.speed(2)

    turn = [1, 2, 3, 4]

    for i in turn:
        my_square.forward(100)
        my_square.right(90)


def draw_triangle():
    my_triangle = turtle.Turtle()
    my_triangle.shape("arrow")
    my_triangle.color("blue")
    my_triangle.speed(5)

    turn = [1, 2, 3]

    for i in turn:
        my_triangle.right(120)
        my_triangle.forward(200)


def draw_shapes():

    window = turtle.Screen()
    window.bgcolor("white")

    draw_square()
    draw_circle()
    draw_triangle()

    window.exitonclick()


draw_shapes()