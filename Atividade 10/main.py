import pygame, sys
from pygame.locals import QUIT
 
# lista de números que vai ser analisada pelo histograma
nums = [
    100, 120, 130, 120, 150, 100, 160, 200, 190, 110, 115, 125, 135, 170, 130
]
# quantidade de faixas
num_cat = 4
# ponto inicial da primeira faixa
num_min = min(nums)
# ponto final da ultima faixa
num_max = max(nums)
# largura de cada faixa
tam_cat = (num_max - num_min) / num_cat
# total de números em cada uma das faixas
lista_total = [0] * num_cat
 
 
# conta quantos números da lista vão em cada faixa
def contabiliza_totais(nums, lista_total):
    for i in range(len(nums)):
# o maior número fica no limite da última faixa
        if nums[i] == num_max:
# soma mais um na última faixa
            lista_total[-1] += 1
# vai para o próximo número
            continue
 
        for i_cat in range(num_cat):
#define que o limite inferior é o menor número mais a posição da faixa vezes o tamanho da faixa
            lim_inf = num_min + i_cat * tam_cat
#define que o limite superior é o maior nímero mais o tamanho da faixa
            lim_sup = lim_inf + tam_cat
 
#vê em qual faixa o número está
            if lim_inf <= nums[i] < lim_sup:
                lista_total[i_cat] += 1
#se encontrou a faixa certa não precisa ficar vendo as outras
                break
# retorna a lista 
    return lista_total

print(contabiliza_totais(nums, lista_total))
 
 
#desenha as barras do histograma
def draw(screen):
#altura da janela
    screen_h = screen.get_height()
    for i in range(len(lista_total)):
#as barras começam e em 100 e cada uma fica a 50 pixels da outra
        x = 100 + i * 50
# define a altura da barra e que cada elemento vale 20 pixels
        h = 20 * lista_total[i]
#desenha a barra vermelha
        pygame.draw.rect(screen, (255, 0, 0), (x, screen_h - h - 80, 25, h))
 
lista_nums = [
    100, 120, 130, 120, 150, 100, 160, 200, 190, 110, 115, 125, 135, 170, 130
]
#pede para o usuário um número
num = int(input("Digite um número"))
#adciona o número na lista 
lista_nums.append(num)
 
pygame.init()
#cria a janela
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
while True:
    for event in pygame.event.get():
#define que, se o usuário clicar no X da tela, encerra o pygame
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
#desenha as barras
    draw(screen)
    pygame.display.update()