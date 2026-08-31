from turtle import *

t = Turtle()
#plano cartesiano
#x direita
t.pd()
t.goto (400,0)
t.stamp()
t.pu()

# y cima
t.lt(90)
t.goto(0,400)
t.pd()
t.stamp()
t.goto(0,-400)
t.rt(180)
t.stamp()
t.rt(90)
t.pu()
t.goto(-400,0)
t.stamp()
t.pd()
t.goto(0,0)
t.rt(180)


#formas
t.shape("turtle")
t.pu()
t.goto(150, 100)

t.pd()
c = textinput("Escolha da cor","Escolha a cor da próxima forma")
cf = textinput("Escolha da borda","Escolha a cor da borda da forma")
t.color(cf)
t.fillcolor(c)
# t.color("pink")
# t.fillcolor("black")
t.begin_fill()
for cont in range (12):
    t.fd(50)
    t.lt(30)
t.end_fill()

t.pu()
t.goto(-250, 100)
c = textinput("Escolha da cor","Escolha a cor da próxima forma")
cf = textinput("Escolha da borda","Escolha a cor da borda da forma")
t.color(cf)
t.fillcolor(c)
# t.color("black")
# t.fillcolor("yellow")

t.pd()
t.begin_fill()
for count in range (3):
    t.fd(100)
    t.lt(120)
t.end_fill()

t.pu()
t.goto(-200, -200)
c = textinput("Escolha da cor","Escolha a cor da próxima forma")
cf = textinput("Escolha da borda","Escolha a cor da borda da forma")
t.color(cf)
t.fillcolor(c)

t.pd()
t.begin_fill()
for count in range(5):
    t.fd(50)
    t.lt(72)
t.end_fill()

t.pu()
t.goto(200, -200)
c = textinput("Escolha da cor","Escolha a cor da próxima forma")
cf = textinput("Escolha da borda","Escolha a cor da borda da forma")
t.color(cf)
t.fillcolor(c)

t.pd()
t.begin_fill()
for count in range(6):
    t.fd(50)
    t.lt(60)
t.end_fill()

t.pu()
t.goto(300,-200)
c = textinput("Escolha da cor","Escolha a cor da espiral")
t.color(c)
t.fillcolor(c)
t.pd()
for count in range(300):
    t.forward(count * 2)
    t.left(40)

mainloop()