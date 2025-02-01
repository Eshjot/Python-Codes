import turtle

# object tr for turtle
tr = turtle.Turtle()
tr.hideturtle()
# set thickness for each ring
tr.pensize(3)

tr.color("blue")
tr.penup()
tr.goto(-100, -15)
tr.pendown()
tr.circle(45)

tr.color("black")
tr.penup()
tr.goto(0, -15)
tr.pendown()
tr.circle(45)

tr.color("red")
tr.penup()
tr.goto(100, -15)
tr.pendown()
tr.circle(45)

tr.color("yellow")
tr.penup()
tr.goto(-45, -55)
tr.pendown()
tr.circle(45)

tr.color("green")
tr.penup()
tr.goto(50, -60)
tr.pendown()
tr.circle(45)
