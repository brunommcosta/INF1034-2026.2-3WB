import turtle
from random import randint


def randomColor():
  return (randint(0, 255), randint(0, 255), randint(0, 255))


def drawSquare(t, size):
  # t.goto(x, y)
  t.pd()
  t.begin_fill()
  t.fillcolor(randomColor())
  for i in range(4):
    t.fd(size)
    t.right(90)
  t.end_fill()
  t.pu()


def drawSquareFractal(t, size, step=50):
  if step < 0 or size < 1:
    return
  t.pd()
  t.fd(size / 1.5)
  t.lt(10)
  drawSquare(t, size)
  drawSquareFractal(t, size - 1, step - 1)


def drawSpiral(t):
  for i in range(100):
    t.fd(i)
    t.lt(15)


def drawStarFractal(t, size):
  #deminui o tamanho de tolerancia para poder ter mais estrelas no fractal
  if size < 2:
    return
  for i in range(5):
    drawStarFractal(t, size / 3)
    t.fd(size)
    t.lt(216)


def treeFractal(t, size, angle, nivel):
  if size < 10:
    return
  t.pd()
  t.pencolor(0, 255 // max(nivel, 1), 0)
  t.fd(size)                      
  # ramo da direita
  t.rt(angle)
  treeFractal(t, size * 0.7, angle, nivel - 1)
  # ramo do centro
  t.lt(angle) #gira o mesmo ângulo, mas só uma ve para apontar a tartaruga para cima                    
  treeFractal(t, size * 0.7, angle, nivel - 1)
  # ramo da esquerda
  t.lt(angle)
  treeFractal(t, size * 0.7, angle, nivel - 1)
  t.rt(angle)                     

def floco_de_neve(t, size, nivel):
  if size < 4:
    return
  t.pd()
  t.fd(size)#mesmo princípio da árvore só que no código eu faço um for dele 
  # ramo da esquerda
  t.lt(60)
  floco_de_neve(t, size * 0.45, nivel - 1)
  t.rt(60)
  # ramo do centro (continua a haste)
  floco_de_neve(t, size * 0.45, nivel - 1)
  # ramo da direita
  t.rt(60)
  floco_de_neve(t, size * 0.45, nivel - 1)
  t.lt(60)
  t.bk(size)      


t = turtle.Turtle()
turtle.colormode(255)
# t.speed("slowest")
t.speed(0)
t.pu()

## Desenhando o "chifre"
# t.goto(-100, -200)
# t.pd()
# drawSquareFractal(t, 70, 60)

## Desenhando a estrela
# t.color("pink")
# t.goto(-100, 0)
# t.pd()
# drawStarFractal(t, 200)

## Desenhando a árvore
# t.goto(0, -200)
# t.lt(90)
# treeFractal(t, 100, 15, 20)

t.goto(0,0)
for i in range(6):
  floco_de_neve(t,100,5)
  t.lt(60)
## Desenhando uma espiral
# drawSpiral(t)
turtle.mainloop()