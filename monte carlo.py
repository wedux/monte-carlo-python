from turtle import *
from random import *
from math import sqrt

def kwadrat(dl):
    for i in range(4):
        lt(90)
        fd(dl)
speed(0)
setup(1200, 1000)
title("Metoda Monte Carlo")
kwadrat(400)
lt(90)
up()
fd(400/2)
down()
circle(400/2)


ht()
tracer(5)
for i in range(1, 51):
    pktCircle = 0
    up()
    x = randint(-400, 0)
    y = randint(0, 400)
    goto(x, y)
    down()

    
    if sqrt(x**2 + y**2) <= 200:
        dot(5, "blue")
    else:
        dot(5, "red")

