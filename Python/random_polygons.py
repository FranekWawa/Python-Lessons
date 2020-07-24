from graphics import *
import random
import math


def polyPoints(sides,radius, x_centre,y_centre):
    angle = math.radians(0)
    angle_increment = math.radians(360/sides)
    points = []
    
    for i in range(sides):
        x = x_centre + radius * math.cos(angle)
        y = y_centre + radius * math.sin(angle)
        angle += angle_increment
        points.append(Point(x,y))
    return points
        
def randColor():
    r = random.randint(0,255)
    g = random.randint(0,255)    
    b = random.randint(0,255)
    return color_rgb(r,g,b)

def main():
    win = GraphWin("My Circle", 500, 500)
    win.setBackground('blue')
    
    #iterations
    i=0
    #store objects
    shapes = []
    
    while True:
        #count iterations
        i+=1
        
        #get cursor position 
        Cursor = win.getMouse()
        x = Cursor.getX()
        y = Cursor.getY()
        
        #random color
        color = randColor()

        #random shapes
        number = random.randint(2,10)
        if number == 2:
            s = Circle(Cursor, 20)
        if number > 2:
            points = polyPoints(number, 20,x,y)
            s = Polygon(points)
            
        #drawing and saving shapes
        s.setFill(color)
        s.draw(win)
        shapes.append(s)

        #change color of previous objects
        if i == 5:
            for shape in shapes[:-1]:
                shape.undraw()
                shape.setFill(randColor())
                shape.draw(win)
            i = 0    
    

main()
