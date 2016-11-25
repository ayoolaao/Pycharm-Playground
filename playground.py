import turtle


def draw_square():

    window = turtle.Screen()
    window.bgcolor("#80CDFF")

    ayo = turtle.Turtle()
    ayo.shape("turtle")
    ayo.color("#000000")
    ayo.speed(2)

    turn = [1 ,2, 3, 4]

    for i in turn:
        ayo.forward(100)
        ayo.right(90)

    window.exitonclick()

draw_square()