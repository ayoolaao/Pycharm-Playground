import turtle


def draw_square(my_square):

    for i in range(1,5):
        my_square.speed(0.5)
        my_square.color("#6DB25D")
        my_square.forward(100)
        my_square.right(90)


def draw_shapes():

    window = turtle.Screen()
    window.bgcolor("#A83623")

    ayo = turtle.Turtle()
    for i in range(0,36):
        draw_square(ayo)
        ayo.right(10)

    window.exitonclick()


draw_shapes()