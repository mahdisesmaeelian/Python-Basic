import turtle
t = turtle.Pen()
t.shape('turtle')
t.penup()
t.goto(0,100)
t.pendown()

position1=0
position2=100
zel=3
i = 1

while zel<10:
    for i in range(zel):         
        t.forward(80)
        t.right(360/zel)

    zel+=1
    position1+=1
    position2+=10
    t.penup()
    t.goto(position1,position2)
    t.pendown()
 
   
        