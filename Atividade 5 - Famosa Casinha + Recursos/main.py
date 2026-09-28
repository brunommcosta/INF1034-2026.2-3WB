from pygame import *

init()
screen=display.set_mode((800, 600))
#Recursos aramezenar todos em variáveis
minhaImagem=image.load("sailor moon.png")
minhaImagem=transform.scale(minhaImagem, (400//3,732//3))
minhaFonte=font.Font("MonimerSerif.otf",25)
mixer.music.load("abertura sailor moon.mp3")
mixer.music.play(-1)

running=True
while running:
    #time.clock.tick(60)
    for ev in event.get():
        if ev.type == QUIT:
            running = False

    #Parte para desenhar na tela
    screen.fill("#97D1FA")
            #superficie,cor,(x,y,larg,alt)
    draw.rect(screen,"#489D25",(0,500,800,100))
    draw.rect(screen,"#646464",(200,300,200,200))
    draw.circle(screen,"#FFF251",(100,100), 30)
    draw.polygon(screen,"#F2883B",((200,300),(400,300),(300,150)))
    draw.line(screen,"#FFF251",(40,40),(155,155),4)
    draw.line(screen,"#FFF251",(100,40),(100,155),4)
    draw.line(screen,"#FFF251",(40,100),(155,100),4)
    draw.line(screen,"#FFF251",(155,40),(40,155),4)
    draw.circle(screen,"#FFFFFF",(500,100), 30)
    draw.circle(screen,"#FFFFFF",(525,100), 30)
    draw.circle(screen,"#FFFFFF",(550,100), 30)
    draw.circle(screen,"#FFFFFF",(575,100), 30)
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

