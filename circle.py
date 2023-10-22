import turtle

bob = turtle.Turtle()
print(bob)

def polygon(t,length,n):
    angle=360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

import math
def circle(t,r):
    circm=2*math.pi*r
    n = int(circm/3)+1
    length=circm/n
    polygon(t,length,n)
circle(turtle,100)

turtle.mainloop()