import turtle
import turtle as t

t.speed(20)
pattern=0
scr=turtle.Screen()
scr.bgcolor("yellow")
for i in range(100):
    for color in  ["blue","green"]:
        t.color(color)
        t.forward(pattern)
        t.right(90)
        t.right(1)
        pattern+=1
turtle.done()