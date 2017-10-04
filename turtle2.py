from turtle import *
Pen()
color('yellow','red')

begin_fill()

while True:
    forward(400)
    left(160)
    if abs(pos()) < 1 :
        end_fill()
        break
