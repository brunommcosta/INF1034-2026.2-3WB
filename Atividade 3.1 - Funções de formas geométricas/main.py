from turtle import *
import random
def desenha_plano():
    t.pu()
    t.goto(-400, 0)
    t.pd()
    t.goto(400, 0)
    t.stamp()
    t.pu()
    t.goto(0, -400)
    t.pd()
    t.goto(0, 400)
    t.lt(90)
    t.stamp()
    t.rt(90)
    t.pu()
    t.goto(0,0)
    t.pd()

def desenha_ret(comprimento, largura, c):
    t.setheading(0)
    t.fillcolor(c)
    t.begin_fill()
    for cont in range (2):
        t.fd(comprimento)
        t.lt(90)
        t.fd(largura)
        t.lt(90)
    t.end_fill()

def desenha_tri(x,y,tamanho,cor):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.fillcolor(cor)
    t.begin_fill()
    for cont in range(3):
        t.fd(tamanho)
        t.lt(120)
    t.end_fill()

def desenha_circulo(raio,x,y,cor):
    t.setheading(0)
    t.goto(x,y)
    t.pd()
    t.fillcolor(cor)
    t.begin_fill()
    t.circle(raio)
    t.end_fill()

def desenha_hex(x,y,tamanho,cor):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.setheading(0)
    t.fillcolor(cor)
    t.begin_fill()
    for count in range(6):
        t.fd(tamanho)
        t.lt(60)
    t.end_fill()

def desenha_poligono(x,y, lados, tamanho,cor):
    t.pu()
    t.goto(x,y)
    t.pd()
    angulo = 360 / lados
    t.fillcolor(cor)
    t.begin_fill()
    for _ in range(lados):
        t.forward(tamanho)
        t.lt(angulo)
    t.end_fill()

def desenha_spiral(x,y,cor):
    t.pu()
    t.goto(x,y)
    t.color(cor)
    t.pd()
    for count in range(300):
        t.forward(count * 2)
        t.left(40)

t = Turtle()
desenha_plano()

#formas
t.shape("turtle")
x4=random.randint(0,400)
y4=random.randint(0,400)
desenha_poligono(x4,y4,12,50,"purple")
t.pu()
x=random.randint(-400,0)
y=random.randint(0,400)
desenha_tri(x,y,50,"pink")
x1=random.randint(-400,0)
y1=random.randint(-400,0)
desenha_poligono(x1,y1,5,20,"yellow")
x2=random.randint(0,400)
y2=random.randint(-400,0)
desenha_hex(x2,y2,30,"blue")
x3=random.randint(0,400)
y3=random.randint(0,400)
desenha_spiral(x3,y3,"black")

mainloop()