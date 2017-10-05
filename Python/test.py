from graphics import *

def main():
    win = GraphWin('FACE', 400, 400) # give title and dimensions
    win.yUp() # make right side up coordinates!


    eye2 = Line(Point(45, 105), Point(55, 105)) # set endpoints
    eye2.setWidth(3)
    eye2.draw(win)

main()
