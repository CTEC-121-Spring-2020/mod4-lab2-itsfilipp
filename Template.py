"""
CTEC 121
<your name>
<assignment/lab name>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""
from graphics import *

def main():
    '''
    startValue = 1
    endValue = 10
    sum = 0
    for i in range(startValue, endValue, 2):
        sum = sum + i
    print(sum)
    '''
    win = GraphWin("Demo", 800, 800)
    win.setCoords(-4.0, -4.0, 4.0, 4.0)
    p1 = Circle(Point(2,3), 0.1)
    p1.setFill("red")
    p1.draw(win)
    p2 = Point(-3,1).draw(win)
    p3 = Point(-1.5, -2.5).draw(win)

    input()

main()    