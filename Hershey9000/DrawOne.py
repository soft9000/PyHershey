# MISSION: Show how to draw a Hershey character using Hershey9000.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: See https://github.com/soft9000/PyHershey
# DATE: 2026-05-28 09:51:00
# FILE: DrawOne.py
# AUTHOR: See https://ko-fi.com/randallnagy
#
import turtle
from Hershey9000.VectorFont.Font import Font

INVERT = True # Switch between coordinate plans
scale = 10
pw_font = 0; which_glyph = 3
font = Font.Load_Font(font_names[pw_font])
line = font.get_glyph(which_glyph)
turtle.pensize(6)
inset = 100
for ss, point in enumerate(line):    
    if ss % 2 == 0:
            turtle.penup()
    else:
        turtle.color("black")
        turtle.pendown()
    point = (scale * point[0] - inset,
             scale * point[1] - inset)
    if INVERT:
        # Modern Computer Plane:
        turtle.goto(
            point[0],
            point[1] * -1
        )
    else:
        # Cartesian Classics:
        turtle.goto(
            point[0],
            point[1]
        )        
    turtle.penup()
