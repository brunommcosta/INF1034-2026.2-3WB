import pygame, sys
from pygame.locals import QUIT

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((800, 600))

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
lugar_x, lugar_y = lugares.pop(lugar_jogador)
hero_x = lugar_x
hero_y = lugar_y
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

vilao_idle_spritesheet = idle_spritesheet.copy()
vilao_run_spritesheet = run_spritesheet.copy()
vilao_idle_spritesheet.fill((255, 110, 110), special_flags=pygame.BLEND_RGB_MULT)
vilao_run_spritesheet.fill((255, 110, 110), special_flags=pygame.BLEND_RGB_MULT)

margem_x = 40
margem_y = 20
esq_x = bloco_esq_x - W - margem_x
dir_x = bloco_dir_x + largura_bloco + margem_x
meio_x = (esq_x + dir_x)//2
cima_y = inicio_y - H - margem_y
baixo_y = inicio_y + altura_bloco + margem_y
meio_y = (cima_y + baixo_y)//2

pontos = [
    (esq_x, cima_y, Direita),
    (meio_x, cima_y, Baixo),
    (dir_x, cima_y, Esquerda),
    (dir_x, meio_y, Esquerda),
    (dir_x, baixo_y, Esquerda),
    (meio_x, baixo_y, Cima),
    (esq_x, baixo_y, Direita),
    (esq_x, meio_y, Direita),
]

vilao_x = pontos[0][0]
vilao_y = pontos[0][1]
vilao_speed = 1
vilao_direction = Direita
vilao_andando = True
vilao_was_andando = True
ponto_alvo = 1
vilao_tempo_parado = 0
tempo_observando = 2000
vilao_ja_viu = False
vilao_frame = 0
vilao_anim_time = 0

tolerancia_lugar = 16
advertencias = 0
aviso_tempo = 0
duracao_aviso = 3000
fonte = pygame.font.Font(None, 30)
fonte_grande = pygame.font.Font(None, 56)

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

    if aviso_tempo > 0:
        aviso_tempo = aviso_tempo - dt

    if vilao_andando:
        alvo_x = pontos[ponto_alvo][0]
        alvo_y = pontos[ponto_alvo][1]
        dist_x = alvo_x - vilao_x
        dist_y = alvo_y - vilao_y

        if dist_x != 0:
            passo = min(vilao_speed, abs(dist_x))
            if dist_x > 0:
                vilao_x += passo
                vilao_direction = Direita
            else:
                vilao_x -= passo
                vilao_direction = Esquerda
        elif dist_y != 0:
            passo = min(vilao_speed, abs(dist_y))
            if dist_y > 0:
                vilao_y += passo
                vilao_direction = Baixo
            else:
                vilao_y -= passo
                vilao_direction = Cima
        else:
            vilao_andando = False
            vilao_tempo_parado = 0
            vilao_ja_viu = False
            vilao_direction = pontos[ponto_alvo][2]
    else:
        vilao_tempo_parado = vilao_tempo_parado + dt

        if not vilao_ja_viu:
            if abs(hero_x - lugar_x) > tolerancia_lugar or abs(hero_y - lugar_y) > tolerancia_lugar:
                vilao_ja_viu = True
                advertencias = advertencias + 1
                aviso_tempo = duracao_aviso

        if vilao_tempo_parado >= tempo_observando:
            vilao_andando = True
            ponto_alvo = (ponto_alvo + 1) % len(pontos)
            vilao_speed=vilao_speed+0.05

    if vilao_andando != vilao_was_andando:
        vilao_frame = 0
        vilao_anim_time = 0
    vilao_was_andando = vilao_andando

    vilao_anim_time = vilao_anim_time + dt
    if vilao_andando:
        vilao_intervalo = 0.1
    else:
        vilao_intervalo = 0.2
    if vilao_anim_time/1000 > vilao_intervalo:
        vilao_frame = vilao_frame + 1
        if vilao_frame > frames - 1:
            vilao_frame = 0
        vilao_anim_time = 0

    screen.fill((255, 255, 255))

    for i in range(len(npcs)):
        npc_x, npc_y = npcs[i]
        npc_col = Baixo * frames + (npc_frame + i) % frames
        screen.blit(npc_spritesheet, (npc_x, npc_y),
                    (W * npc_col, 0, W, H))

    vilao_col = vilao_direction * frames + vilao_frame
    if vilao_andando:
        screen.blit(vilao_run_spritesheet, (vilao_x, vilao_y),
                    (W * vilao_col, 0, W, H))
    else:
        screen.blit(vilao_idle_spritesheet, (vilao_x, vilao_y),
                    (W * vilao_col, 0, W, H))

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

    texto_adv = fonte.render(f"Advertências: {advertencias}", True, (0, 0, 0))
    screen.blit(texto_adv, (10, 10))

    if aviso_tempo > 0:
        exclamacao = fonte_grande.render("!", True, (220, 0, 0))
        screen.blit(exclamacao, (vilao_x + W//2 - exclamacao.get_width()//2, vilao_y - 30))

    pygame.display.update()
