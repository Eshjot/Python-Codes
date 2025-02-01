import turtle
width =int(input("Enter the value of width \n"))   #entering the values of width and height from user
height= int(input("Enter the value of height \n")) 
x = 100
y =100

def draw_pattern(w,h):  #created function draw_pattern and passed arguments w and h
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.setheading(180)
    turtle.forward(w)
    turtle.setheading(270)
    turtle.forward(h)
    turtle.setheading(360)
    turtle.forward(w)
    turtle.setheading(90)
    turtle.forward(h)

    # creating middle square 
    turtle.penup()
    turtle.goto(x-30,y-30)
    turtle.pendown()
    turtle.setheading(180)
    turtle.forward(w-60)
    turtle.setheading(270)
    turtle.forward(h-60)

    turtle.setheading(360)
    turtle.forward(w-60)

    turtle.setheading(90)
    turtle.forward(h-60)

    turtle.penup()
    turtle.goto(x-60, y-60)
    turtle.pendown()
    turtle.begin_fill()
    turtle.setheading(180)
    turtle.forward(w-120)
    turtle.setheading(270)
    turtle.forward(h-120)
    turtle.setheading(360)
    turtle.forward(w-120)
    turtle.setheading(90)
    turtle.forward(h-120)
    turtle.end_fill()

    #middle line from left to right 
    turtle.penup()
    turtle.goto(x-w/2,y)
    turtle.pendown()
    turtle.setheading(270)
    turtle.forward(h)

    #middle line from top to bottom
    turtle.penup()
    turtle.goto(x, y-h/2)
    turtle.pendown()
    turtle.setheading(180)
    turtle.forward(w)

    #the diagonal line 1
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x-w, y-h)

    #the diagonal line 2
    turtle.penup()
    turtle.goto(x-w,y)
    turtle.pendown()
    turtle.goto(x, y-h)

draw_pattern(width, height) #calling function

turtle.done()

