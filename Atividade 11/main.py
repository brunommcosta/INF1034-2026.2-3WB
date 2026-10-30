from pygame import *

idle_spritesheet = image.load("Idle.png")
walk_spritesheet = image.load("Walk.png")
galinhaSprites = image.load("Baby Chicken Yellow.png")

init()
screen = display.set_mode((800, 600))
display.set_caption('Hello World!')


tamanhoGalinha=16
framesGalinha=4
tamanhoFrame = 32
idleFrames = 4
walkFrames = 6

fileiraDir = 0
fileiraEsqu = 2

hero_x = 400
hero_y = 300
speed = 0.3
galinhaPlaying=False
galinhaAnimTime=0
galinhaCurrFrame=0
direita = True
walking = False
parouAndar = False

curr_frame = 0
tempo = 0

while True:
    clock=time.Clock()

    for evento in event.get():
        clock.tick(60)
        dt = clock.get_time()
        if evento.type == QUIT:
                quit()
        if evento.type == MOUSEBUTTONDOWN:
            if evento.button == 1 and not galinhaPlaying:
                galinhaPlaying = True
            if galinhaPlaying:
                galinhaAnimTime = galinhaAnimTime + dt

            if galinhaAnimTime > 15:
                galinhaCurrFrame = galinhaCurrFrame + 1
                if galinhaCurrFrame > framesGalinha - 1:
                    galinhaCurrFrame = 0
                    galinhaPlayin = False   
                galinhaAnimTime = 0



    keys=key.get_pressed()
    walking = False

    if keys[K_RIGHT]:
        hero_x += speed
        direita = True
        walking = True
    if keys[K_LEFT]:
        hero_x -= speed
        direita = False
        walking = True

    if walking != parouAndar:
        curr_frame = 0
        tempo = 0
    parouAndar = walking

    tempo = tempo + dt
    tempo_sec = tempo/10000

    if walking:
        total = walkFrames
        intervalo = 0.25
    else:
        total = idleFrames
        intervalo = 0.45  

    if tempo_sec > intervalo:
        curr_frame = curr_frame + 1
        if curr_frame > total - 1:
            curr_frame = 0
        tempo = 0

    screen.fill((255, 255, 255))

    if walking:
        if direita:
            linha = fileiraDir
        else:
            linha = fileiraEsqu
        screen.blit(walk_spritesheet, (hero_x, hero_y),
                    (tamanhoFrame * curr_frame, tamanhoFrame * linha, tamanhoFrame, tamanhoFrame))
    else:
        if direita:
            screen.blit(idle_spritesheet, (hero_x, hero_y),
                        (tamanhoFrame * curr_frame, 0, tamanhoFrame, tamanhoFrame))
    
    screen.blit(galinhaSprites, (600, 300),
                (tamanhoGalinha * galinhaCurrFrame, 0, tamanhoGalinha, tamanhoGalinha))

    display.update()
