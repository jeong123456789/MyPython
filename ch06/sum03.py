fig = int(input("몇각형을 그릴가요"))

import turtle

t = turtle.Turtle()

for i in range(fig):
    t.forward(100)
    t.left(360/fig)
    
