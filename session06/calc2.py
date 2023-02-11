# Exercise 02
import turtle

leo = turtle.Turtle()



def square(t, length):
    """Write a function called square that takes a parameter named t, which is a turtle. It should use the turtle to draw a square"""
    """Adding a parameter to a function is called generalization """
    for i in range(4):
        t.fd(length)
        t.rt(90)

def polyline(t, n, length, angle):
    """Draws n line segments with the given length and
    angle (in degrees) between them. t is a turtle."""
    for i in range(n):
        t.fd(length)
        t.rt(angle)
# polyline(leo,40,20,350)
# square(leo,10)

# Encapsulationraphel=turtle.Turtle()
# square(raphel)


def polygon(t, length, n):
    """made a function to generate polygun with parameter t, length ,n"""
    # for i in range (n):
    #     # t.fd(length)
    #     # t.rt(360/n)
    angle = 360 / n
    polyline(t, n, length, angle)


# polygon(leo,5,100)


import math


def circle(t, r):
    "made a function to generate circle  with radius by using help of polygun function"
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, length, n)




def arc(t, r, angle):
    """a more general version of circle,which determines what fraction of a circle to draw"""
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle =float(angle) / n
    # for i in range (n):
    #     t.fd(step_length)
    #     t.rt(step_angle)
    polyline = (t, n, step_length,step_angle)

arc(leo,20,90)


def move(t, x, y):
    """Move Turtle (t) forward (x, y) units without leaving a trail.
    Leaves the pen down.
    """
    t.pu()
    t.setpos(x, y)
    t.pd()


# arc(leo,20,360)
if __name__ == "__main__":
    print("hello")


turtle.mainloop



# polyline(leo,5,10,250)
