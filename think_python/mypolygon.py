import math

from swampy.TurtleWorld import *


def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)


def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        fd(t, length)
        lt(t, angle)


def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)

world = TurtleWorld()
bob = Turtle()
print(bob)

for i in range(4):
    fd(bob, 100)
    lt(bob)

square(bob, 120)
polygon(bob, 7, 70)
circle(bob, 60)
wait_for_user()