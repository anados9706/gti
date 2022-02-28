from turtle import *
import math

def X2Y(x):
    return (x/40) ** 2
    
def tGoTo(x, y):
    print ("X=", x)
    print ("Y=", y)
    angle= towards(x, y)
    setheading(angle)
    cx, cy = pos()
    xDiff = abs(cx - x)
    yDiff = X2Y(x)
    Distance = math.sqrt((xDiff ** 2)+( yDiff ** 2))
    forward(Distance)   

color('orange', 'pink')
home()

for x in range(100):
    tGoTo(x,40 * X2Y(x))

tGoTo(0, 0)
end_fill()
done()    