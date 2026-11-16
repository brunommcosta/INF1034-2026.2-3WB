import pygame, sys
from pygame.locals import QUIT

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hello World!')

escala = 2

idle_spritesheet = pygame.image.load("Bob_idle_anim_16x16.png")
run_spritesheet = pygame.image.load("Bob_run_16x16.png")
npc_spritesheet = pygame.image.load("Alex_idle_anim_16x16.png")

idle_spritesheet = pygame.transform.scale(idle_spritesheet,
    (idle_spritesheet.get_width() * escala, idle_spritesheet.get_height() * escala))
run_spritesheet = pygame.transform.scale(run_spritesheet,
    (run_spritesheet.get_width() * escala, run_spritesheet.get_height() * escala))
npc_spritesheet = pygame.transform.scale(npc_spritesheet,
    (npc_spritesheet.get_width() * escala, npc_spritesheet.get_height() * escala))

W = 16 * escala
H = 32 * escala
frames = 6

Direita = 0
Cima = 1
Esquerda = 2
Baixo = 3

corredor = 200
colunas_por_bloco = 2
fileiras = 3
espaco_x = 16
espaco_y = 32

largura_bloco = colunas_por_bloco * W + (colunas_por_bloco - 1) * espaco_x
altura_bloco = fileiras * H + (fileiras - 1) * espaco_y
bloco_esq_x = 400 - corredor//2 - largura_bloco
bloco_dir_x = 400 + corredor//2
inicio_y = (600 - altura_bloco)//2

lugares = []
for bloco_x in (bloco_esq_x, bloco_dir_x):
    for fileira in range(fileiras):
        for coluna in range(colunas_por_bloco):
            x = bloco_x + coluna * (W + espaco_x)
            y = inicio_y + fileira * (H + espaco_y)
            lugares.append((x, y))

lugar_jogador = 3
hero_x, hero_y = lugares.pop(lugar_jogador)
direction = Baixo
npcs = lugares

hit_w = W * 3 // 4
hit_h = H // 2
hit_off_x = (W - hit_w)//2
hit_off_y = H - hit_h

npc_rects = []
for i in range(len(npcs)):
    npc_x, npc_y = npcs[i]
    npc_rects.append(pygame.Rect(npc_x + hit_off_x, npc_y + hit_off_y, hit_w, hit_h))

mostrar_hitbox = False

speed = 3
running = False
was_running = False

curr_frame = 0
anim_time = 0

npc_frame = 0
npc_anim_time = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)
    dt = clock.get_time()

    keys = pygame.key.get_pressed()
    running = False
    dx = 0
    dy = 0

    if keys[pygame.K_RIGHT]:
        dx += speed
        direction = Direita
        running = True
    if keys[pygame.K_LEFT]:
        dx -= speed
        direction = Esquerda
        running = True
    if keys[pygame.K_UP]:
        dy -= speed
        direction = Cima
        running = True
    if keys[pygame.K_DOWN]:
        dy += speed
        direction = Baixo
        running = True

    hero_x += dx
    hero_rect = pygame.Rect(hero_x + hit_off_x, hero_y + hit_off_y, hit_w, hit_h)
    if hero_rect.collidelist(npc_rects) != -1:
        hero_x -= dx

    hero_y += dy
    hero_rect = pygame.Rect(hero_x + hit_off_x, hero_y + hit_off_y, hit_w, hit_h)
    if hero_rect.collidelist(npc_rects) != -1:
        hero_y -= dy

    if running != was_running:
        curr_frame = 0
        anim_time = 0
    was_running = running

    anim_time = anim_time + dt
    anim_time_sec = anim_time/1000

    if running:
        frame_interval = 0.1
    else:
        frame_interval = 0.2
    if anim_time_sec > frame_interval:
        curr_frame = curr_frame + 1
        if curr_frame > frames - 1:
            curr_frame = 0
        anim_time = 0

    npc_anim_time = npc_anim_time + dt
    if npc_anim_time/1000 > 0.2:
        npc_frame = npc_frame + 1
        if npc_frame > frames - 1:
            npc_frame = 0
        npc_anim_time = 0

    screen.fill((255, 255, 255))

    for i in range(len(npcs)):
        npc_x, npc_y = npcs[i]
        npc_col = Baixo * frames + (npc_frame + i) % frames
        screen.blit(npc_spritesheet, (npc_x, npc_y),
                    (W * npc_col, 0, W, H))

    frame_col = direction * frames + curr_frame
    if running:
        screen.blit(run_spritesheet, (hero_x, hero_y),
                    (W * frame_col, 0, W, H))
    else:
        screen.blit(idle_spritesheet, (hero_x, hero_y),
                    (W * frame_col, 0, W, H))

    if mostrar_hitbox:
        for rect in npc_rects:
            pygame.draw.rect(screen, (255, 0, 0), rect, 1)
        pygame.draw.rect(screen, (0, 0, 255),
                         (hero_x + hit_off_x, hero_y + hit_off_y, hit_w, hit_h), 1)

    pygame.display.update()
