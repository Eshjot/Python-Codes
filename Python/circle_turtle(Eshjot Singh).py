import turtle

turtle.bgcolor("yellow") #This is the background color
radius= turtle.numinput("radius","Enter the radius value")  #creating variable
angle1= turtle.numinput("angle1","Enter the value of angle1")
angle2= turtle.numinput("angle2","Enter the value of angle2")

turtle.pensize(5) #This refers the size of pen

turtle.color("red")  #Color of the circle
turtle.circle(radius) #radius is variable to be entered by the user

turtle.right(angle1) #Turning pen to right angle

turtle.color("green") #Color of the circle
turtle.circle(radius) #radius is variable to be entered by the user

turtle.left(angle2) #Turning pen to left angle

turtle.color("blue") #Color of the circle
turtle.circle(radius) #radius is variable to be entered by the user

turtle.penup()
turtle.goto(-30,-110)
turtle.pendown()
turtle.write("Eshjot Singh") #writing name in drawing

turtle.done()