''' Show off Hershey's font effort using Python's Turtle Graphics '''

import turtle
from VectorFont.Font import Font

num_msec = 1000

turtle2 = turtle.Turtle()
turtle3 = turtle.Turtle()
turtle4 = turtle.Turtle()

turtles = (turtle, turtle2, turtle3, turtle4)
for t in turtles:
    t.ht()
    t.penup()

turtle4.color('blue')

show_trace = False # Show EVERY line
font_names = Font.List_Fonts()
pw_font = 0
pw_rect = [0,0,0,0]
font = Font.Load_Font('japanese')
which = 0


def stop_run():
    turtle.bye()


def next_font():
    global font; global pw_font
    global which

    which = 0
    pw_font += 1
    if pw_font >= len(font_names):
        pw_font = 0
    font = Font.Load_Font(font_names[pw_font])
    turtle4.clear()
    turtle3.clear()


def draw_rectangle(zturt, x, y, width, height):
    zturt.up()
    zturt.goto(x, y)
    zturt.down()
    zturt.forward(width)
    zturt.right(90)
    zturt.forward(height)
    zturt.right(90)
    zturt.forward(width)
    zturt.right(90)
    zturt.forward(height)
    zturt.right(90)


def display_info():
    global which; global font; global pw_rect
    turtle4.hideturtle()
    turtle4.clear()
    turtle4.penup()
    turtle4.goto(0, 100)
    turtle4.write("Font: '" + font.font_name + "', Glyph #" + str(which), font=("Arial", 24, "normal"))
    turtle4.st()
    draw_rectangle(turtle4, pw_rect[0], pw_rect[1], pw_rect[0] + pw_rect[2], pw_rect[1] + pw_rect[3])


def replay():
    global which; global num_sec
    global pw_font; global font_names
    global font;  global pw_rect
    global show_trace
    turtle4.clear()
    turtle3.clear()
    scale=8

    if which >= font.glyph_count():
        next_font()

    turtle3.ht() # Hide!
    turtle3.penup()
    turtle3.pensize(8)

    pw_rect = font.calc_rect(which)

    pw_rect[0] *= scale
    pw_rect[1] *= scale
    pw_rect[2] *= scale
    pw_rect[3] *= scale
    print(pw_rect)

    line = font.get_glyph(which)
    for ss, point in enumerate(line):
        if ss % 2 == 0:
            if show_trace is False:
                turtle3.penup()
            else:
                turtle3.pendown()
                turtle3.color('lightgray')
        else:
            turtle3.color("black")
            turtle3.pendown()

        turtle3.goto(
            pw_rect[0] + (scale * point[0]   ),
            pw_rect[1] + (scale*point[1] * -1)
        )
        turtle3.penup()
    which += 1
    display_info()
    turtle3.goto(pw_rect[0], pw_rect[1])
    turtle.ontimer(replay, num_msec)


turtle2.color('green')
turtle2.goto(0, 200)
turtle2.write("VECTOR GRAPHICS", font=("Arial", 24, "normal"))
turtle2.goto(0, 180)
turtle2.write("'n' = next font, 'q' = quit", font=("Arial", 16, "normal"))
draw_rectangle(turtle2, -50, 250, 450, 600)

# Setup events
turtle.onkey(stop_run, "q")
turtle.onkey(next_font, "n")

# Schedule timer
turtle.ontimer(replay, num_msec)

turtle.listen()

turtle.mainloop()