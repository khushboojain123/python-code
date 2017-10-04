import turtle as t
p = t.pen()
p.color('yellow','red')

p.begin_fill()

while True:
    p.forward(400)
    p.left(170)
    if abs(p.pos()) < 1 :
        p.end_fill()
        break

