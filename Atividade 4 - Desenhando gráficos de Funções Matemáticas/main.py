from turtle import *
from time import sleep
t=Turtle()

def desenhaPlanoCartesiano():
    t.color("black")
    t.setheading(0)
    t.pu()
    t.goto(-300,0)
    t.pd()
    t.goto(300,0)
    t.stamp()
    t.pu()
    t.lt(90)
    t.goto(0,-300)
    t.pd()
    t.goto(0,300)
    t.stamp()
    t.pu()
    t.setheading(0)

def calculaSomaDeQuadrados(x):
    return x**3-x**2-x+1

def calculaBahskara(x):
    return x**2-5*x+6

def calculaQuadratica(x):
    return 5-x**2

def calculaExponecial(x):
    return 2**x

def funcaoFracao(x):
    return 1/x

def calculaRaiz(x):
    return x**0.5
t.speed(0)
desenhaPlanoCartesiano()
t.goto(-10*10, calculaSomaDeQuadrados(-10))
t.color("pink")
t.pd()
for x in range (-9,11):
    t.goto(x*10,calculaSomaDeQuadrados(x))
sleep(2)
t.clear()

desenhaPlanoCartesiano()
t.goto(-20*10, calculaBahskara(-20))
t.color("red")
t.pd()
for x in range (-20,24):
    t.goto(x*10,calculaBahskara(x))
sleep(2)
t.clear()

desenhaPlanoCartesiano()
t.goto(-20*10,calculaQuadratica(-20))
t.color("green")
t.pd()
for x in range (-20,21):
    t.goto(x*10,calculaQuadratica(x))
sleep(2)
t.clear()

desenhaPlanoCartesiano()
t.goto(-20*20,calculaExponecial(-20))
t.color("orange")
t.pd()
for x in range (-19,21):
    t.goto(x*20,calculaExponecial(x))
sleep(2)
t.clear()

desenhaPlanoCartesiano()
t.color("#ca7ef2")
t.goto(-100*40, funcaoFracao(-20))
t.pd()
for x in range (-99,0):
    x=x/20
    t.goto(x*40, funcaoFracao(x)*40)
t.pu()
t.goto((1/20)*40,funcaoFracao(1/20)*40)
t.pd()
for x in range (2,151):
    x=x/20
    t.goto(x*40,funcaoFracao(x)*40)
sleep(2)
t.clear()

desenhaPlanoCartesiano()
t.goto (0, calculaRaiz(0))
t.color("blue")
t.pd()
for x in range (0,350):
    x/20
    t.goto(x,calculaRaiz(x))

mainloop()