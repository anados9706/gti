from turtle import *
import math

def x2y(x):
    return x ** 2

if __name__ == "__main__":
    for x in range(400):
        #y = 10 * (x % 10)
        #y = 90 * math.sin(x/40)
        #y = 90 * math.sin((x/40) - 100)
        #y = ((((x - 200)/20)) ** 2)
        y = math.tan(x/20)
        setpos(x, y)

    '''   
    for x in range(399, 0 ,-1):
        y = 90 * abs(math.sin(x/40))
        setpos(x, y)
    '''    
    done()