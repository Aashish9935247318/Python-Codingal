import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("blue")
t.speed(0)
turtle.tracer(4, 0)

colors = ["#E2400E", "#ffb74d", "#FFA726", "#12E948", "#4804C5"] 

for i in range(360):
    t.color(colors [i % 5])
    t.circle(140)
    t.left(1)


turtle.done