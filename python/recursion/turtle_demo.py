import turtle

t = turtle.Turtle()
t_win = turtle.Screen()


def draw(t, line):
    if line > 0:
        t.forward(line)
        t.right(90)
        draw(t, line - 5)


draw(t, 100)
t_win.exitonclick()
