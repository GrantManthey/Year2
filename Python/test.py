from graphics import *

def main():
    win = GraphWin('FACE', 400, 400) # give title and dimensions
    win.yUp() # make right side up coordinates!

    lineone= Line(Point(74, 224), Point(74, 242)) # set endpoints
    lineone.draw(win)
    
    linetwo= Line(Point(76, 224), Point(76, 176))
    linetwo.draw(win)
    
    linethree= Line(Point(77,188), Point(77,166 ))
    linethree.draw(win)
    
   # linefour= Line(Point(, ), Point(, ))
   # linefour.draw(win)
    
    #linefive= Line(Point(, ), Point(, ))
   # linefive.draw(win)
    
   # linesix= Line(Point(, ), Point(, ))
    #linesix.draw(win)
    
    #lineseven= Line(Point(, ), Point(, ))
    #lineseven.draw(win)
    
   # lineeight= Line(Point(, ), Point(, ))
    #lineeight.draw(win)
    
    #linenine= Line(Point(, ), Point(, ))
   # linenine.draw(win)
    
   # lineten= Line(Point(, ), Point(, ))
    #ineten.draw(win)
    
    #lineeleven= Line(Point(, ), Point(, ))
    #lineeleven.draw(win)
    
   # linetwelve= Line(Point(, ), Point(, ))
    #linetwelve.draw(win)
    
    #linethirteen= Line(Point(, ), Point(, ))
    #linethirteen.draw(win)
    
  #  linefourteen= Line(Point(, ), Point(, ))
   # linefourteen.draw(win)
    
 #   linefifteen= Line(Point(, ), Point(, ))
  #  linefifteen.draw(win)
    
 #   linesixteen= Line(Point(, ), Point(, ))
  #  linesixteen.draw(win)
    
   # line= Line(Point(, ), Point(, ))
   # lineseventeen.draw(win)
    
    #lineeighteen= Line(Point(, ), Point(, ))
  #  lineeighteen.draw(win)
    
    message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
    message.draw(win)
    win.getMouse()
    win.close()

main()
