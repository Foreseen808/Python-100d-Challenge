import random
import turtle as turtle_module

color_list = [(129, 196, 197), (53, 80, 222), (170, 225, 238), (180, 1, 50), (65, 211, 154), (170, 210, 162),
              (200, 21, 73), (139, 75, 109), (69, 75, 222), (191, 135, 240)]
turtle_module.colormode(255)
turtle_module.penup()
turtle_module.hideturtle()
turtle_module.setheading(225)
turtle_module.forward(250)
turtle_module.setheading(0)
turtle_module.speed("fastest")
number_of_dots = 100

for count in range (1, number_of_dots + 1):
    turtle_module.dot(20, random.choice(color_list))
    turtle_module.forward(50)
    if count % 10 == 0:
        turtle_module.setheading(90)
        turtle_module.forward(50)
        turtle_module.setheading(180)
        turtle_module.forward(500)
        turtle_module.setheading(0)
turtle_module.Screen().exitonclick()
