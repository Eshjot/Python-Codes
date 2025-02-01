import turtle
def checkerboard():
    turtle.setup(500,500)
    turtle.penup()
    turtle.fillcolor("black")

    line_starting_with_filled_box(-250,250)
    line_starting_with_unfilled_box(-250, 150)
    line_starting_with_filled_box(-250,50)
    line_starting_with_unfilled_box(-250,-50)
    line_starting_with_filled_box(-250,-150)
def filled_box():
    turtle.begin_fill()
    for x in range(4):
        turtle.forward(100) 
        turtle.right(90)
    turtle.end_fill()
def unfilled_box():
    for x in range(4):
        turtle.forward(100) 
        turtle.right(90)  

def line_starting_with_filled_box(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown() 
    filled_box()

    x+=100
    turtle.goto(x,y)
    unfilled_box()
    x+=100
    turtle.goto(x,y)
    filled_box()  
    x+=100
    turtle.goto(x,y)
    unfilled_box() 
    x+=100
    turtle.goto(x,y)
    filled_box()


def line_starting_with_unfilled_box(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()  
    unfilled_box()
    x+=100
    turtle.goto(x,y)
    filled_box() 
    x+=100
    turtle.goto(x,y)
    unfilled_box() 
    x+=100 
    turtle.goto(x,y) 
    filled_box() 
    x+=100
    turtle.goto(x,y)
    unfilled_box()

checkerboard()    

turtle.done()