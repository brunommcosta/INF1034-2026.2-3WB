from pygame import *

init()
screen=display.set_mode((800, 600))
screen=display.set_mode((800, 600))
#Recursos aramezenar todos em variáveis
minhaImagem=image.load("sailor moon.png")
minhaImagem=transform.scale(minhaImagem, (400//3,732//3))
minhaFonte=font.Font("MonimerSerif.otf",25)
mixer.music.load("abertura sailor moon.mp3")
mixer.music.play(-1)
Som1= mixer.Sound("moon healing.mp3")
Som2= mixer.Sound("brilho.mp3")
Som3= mixer.Sound("glitter.mp3")
nuvem_x=500
c="#97D1FA"
##clock=time.clock()
running=True
while running:
    #time.clock.tick(60)
    mouseX,mouseY=mouse.get_pos()
    for ev in event.get():
        if ev.type == QUIT:
            running = False
        if ev.type == MOUSEBUTTONDOWN:
            if ev.button== 1:
                if mouseY<=200:
                    Som3.play()
                elif mouseY<=400:
                    Som2.play()  
                else:
                    Som1.play()

    #Parte de par movimentações e simulações físicas
    #dt=time.clock.get_time()/1000
    keys=key.get_pressed()
    nuvem_x+=0.1
    if nuvem_x>870:
        nuvem_x=-75
    if nuvem_x<-75:
        nuvem_x=870


    #Parte para desenhar na tela
    if mouseY<=200:
        c="#97D1FA"
    elif mouseY<=400:
        c="#EAA949"
    else:
        c="#E35A38"
    screen.fill(c)
    draw.line(screen,"#FFF251",(mouseX-60,mouseY+60),(mouseX+60,mouseY-60),4)
    draw.line(screen,"#FFF251",(mouseX,mouseY-60),(mouseX,mouseY+60),4)
    draw.line(screen,"#FFF251",(mouseX-60,mouseY-60),(mouseX+60,mouseY+60),4)
    draw.line(screen,"#FFF251",(mouseX-60,mouseY),(mouseX+60,mouseY),4)
    draw.rect(screen,"#489D25",(0,500,800,100))
    draw.rect(screen,"#646464",(200,300,200,200))
    draw.circle(screen,"#FFF251",(mouseX,mouseY), 30)
    draw.polygon(screen,"#F2883B",((200,300),(400,300),(300,150)))
    draw.circle(screen,"#FFFFFF",(nuvem_x,100), 30)
    draw.circle(screen,"#FFFFFF",(nuvem_x+25,100), 30)
    draw.circle(screen,"#FFFFFF",(nuvem_x+50,100), 30)
    draw.circle(screen,"#FFFFFF",(nuvem_x+75,100), 30)
    draw.rect(screen,"#C58B05",(300,365,60,135))
    draw.rect(screen,"#4078B8",(230,365,50,50))
    draw.circle(screen,"#000000",(350,432), 5)
    draw.rect(screen,"#583F05",(600,365,40,135))
    draw.circle(screen,"#004F20",(620,339), 90)

    #Desenhar imagem na tela
    screen.blit( minhaImagem, (500, 275))

    #texto
    meuTexto= minhaFonte.render("Superar obstáculos faz as garotas\nmais bonitas, sabia?",True, "#000000")
    screen.blit(meuTexto,(400, 150))


    display.update()

