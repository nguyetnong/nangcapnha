import turtle

import my_grid
my_grid.make_grid(turtle, grid_size = 1000, sub_divisions = 40)

turtle.pensize(2)
turtle.color("blue")
turtle.begin_fill()
a=2
cnt=0
turtle.goto(25,0)
while(cnt<a):
    
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    cnt=cnt+1
turtle.end_fill()

turtle.penup()
turtle.goto(100,-150)
turtle.pendown()
turtle.color("yellow")
turtle.begin_fill()
cnt=0
while(cnt<a):
    
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
    cnt=cnt+1
turtle.end_fill()

turtle.penup()
turtle.goto(25,0)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
turtle.goto(125,100)
turtle.goto(225,0)
turtle.end_fill()

turtle.penup()
turtle.goto(150,50)
turtle.pendown()
turtle.goto(150,80)
turtle.goto(175,80)
turtle.goto(175,25)

turtle.penup()
turtle.goto(175,90)
turtle.pendown()
turtle.goto(175,125)
turtle.penup()
turtle.goto(160,90)
turtle.pendown()
turtle.goto(160,120)

turtle.penup()
turtle.goto(-100,-200)
turtle.pendown()
turtle.color("brown")
turtle.begin_fill()
turtle.goto(-85,-125)
turtle.goto(-65,-125)
turtle.goto(-50,-200)
turtle.goto(-100,-200)
turtle.end_fill()

turtle.color("green")
turtle.begin_fill()
turtle.penup()
turtle.goto(-75,-50)
turtle.pendown() 
turtle.circle(-50,steps=3)
turtle.end_fill()

turtle.penup()
turtle.goto(-75,0)
turtle.pendown()
turtle.begin_fill()
turtle.goto(-50,-50)
turtle.goto(-100,-50)
turtle.goto(-75,0)
turtle.end_fill()

turtle.penup()
turtle.goto(-75,40)
turtle.pendown()
turtle.begin_fill()
turtle.goto(-55,0)
turtle.goto(-95,0)  
turtle.goto(-75,40)
turtle.end_fill()


turtle.done()