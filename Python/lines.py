from graphics import *


#check if cursor position is close to an existing point
def isClose(cursor,point):
    x1 = cursor.getX()
    y1 = cursor.getY()

    x2 = point.getX()
    y2 = point.getY()
    maxDistance = 10
    if x1 > x2:
        if y1 > y2:
            result = x1-x2<=maxDistance and y1-y2<=maxDistance
        if y1 < y2:
            result = x1-x2<=maxDistance and y2-y1<=maxDistance
        if y1 == y2:
            result = x1-x2<=maxDistance
    if x1 < x2:
        if y1 > y2:
            result = x2-x1<=maxDistance and y1-y2<=maxDistance
        if y1 < y2:
            result = x2-x1<=maxDistance and y2-y1<=maxDistance
        if y1 == y2:
            result = x2-x1<=maxDistance
    if x1 == x2:
        if y1 == y2:
            result = True 
        if y1 > y2:
            result = y1-y2<=maxDistance
        if y1 < y2:
            result = y2-y1<=maxDistance
    return result

def main():
    #open a window
    win = GraphWin("Window",500,500)
    #store cursor position
    cursorPos = []
    
    #store lines
    lines = []
    while True:
        #get cursor positions
        Cursor = win.getMouse()
        
        if len(cursorPos) > 0:
            #check if the cursor position is close to an existing point
            close = False
            
            index = 0
            
            for points in cursorPos:
                close = isClose(points,Cursor)
                if close == True:
                    #changes point position
                    newCursor = win.getMouse()
                    cursorPos[index] = newCursor

                    #re-draw corresponding lines
                    if index > 0:
                        if index < len(cursorPos)-1:
                            prevPoint = cursorPos[index-1]
                            nextPoint = cursorPos[index+1]
                            backLine = lines[index-1]
                            frontLine = lines[index]
                            
                            backLine.undraw()
                            frontLine.undraw()
                            
                            backLine = Line(prevPoint,newCursor)
                            frontLine = Line(newCursor,nextPoint)
                            
                            backLine.draw(win)
                            frontLine.draw(win)
                            
                            lines[index-1] = backLine
                            lines[index] = frontLine
                        else:
                            prevPoint = cursorPos[index-1]
                            backLine = lines[index-1]

                            backLine.undraw()

                            backLine = Line(prevPoint,newCursor)

                            backLine.draw(win)

                            lines[index-1] = backLine
                    else:
                        nextPoint = cursorPos[index+1]

                        frontLine = lines[index]

                        frontLine.undraw()

                        frontLine = Line(newCursor,nextPoint)

                        frontLine.draw(win)

                        lines[index] = frontLine
    
                            
                            
                            
                    index+=1
                    break
                index+=1
        
            #draw line
            if close == False:
                lastPoint = cursorPos[-1]
                l = Line(lastPoint,Cursor)
                l.draw(win)
                lines.append(l)
                cursorPos.append(Cursor)
        if len(cursorPos) <= 0:
            cursorPos.append(Cursor)

main()
