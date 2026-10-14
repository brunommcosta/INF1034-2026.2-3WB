from pygame import *
def validarEmail(email):
    return email[-8:] == "@puc.com"

def procuraMaiuscula(senha):
    for i in senha:
        if 'A' <= i <= 'Z':
            return True
    return False

def procuraMinuscula(senha):
    for i in senha:
        if 'a' <= i <= 'z':
            return True
    return False

def procuraNumero(senha):
    for i in senha:
        if '0' <= i <= '9':
            return True
    return False

def validarSenha(senha):
    if len(senha) < 8:
        return False
    if not procuraMinuscula(senha):
        return False
    if not procuraMaiuscula(senha):
        return False
    if not procuraNumero(senha):
        return False

    return True

def criptografaSenha(senha):
    senhaNova = ""
    tamanho = ord('z') - ord('0') + 1     
    for i in senha:
        if '0' <= i <= 'z':
            pos = (ord(i) - ord('0') + 3) % tamanho
            senhaNova += chr(pos + ord('0'))
        else:
            senhaNova += carac
    return senhaNova

init()
screen = display.set_mode((1280, 720))
display.set_caption("Login")
clock = time.Clock()
running = True

minhaImagem=image.load("sailor moon.png")
minhaImagem=transform.scale(minhaImagem, (400//3,732//3))
mixer.music.load("abertura sailor moon.mp3")
#mixer.music.play(-1)
Som1= mixer.Sound("moon healing.mp3")
#Som2= mixer.Sound("brilho.mp3")
Som3= mixer.Sound("glitter.mp3")
digitoEmail = ""
digitoSenha = ""
emailValido = False
senhaValida = False
tentouEmail = False      
tentouSenha = False      
abrirCasinha = False
minhaFonte = font.Font(size= 25)
fonteCasinha=font.Font("MonimerSerif.otf",25)
fonteValidation = font.Font(size=25)

rectEmail = Rect(100, 100, 500, 50)
rectSenha = Rect(100, 200, 500, 50)

while running:
    for ev in event.get():
        if ev.type == QUIT:
            running = False

        if ev.type == KEYDOWN:
            if ev.key == K_BACKSPACE:
                if not emailValido:
                    digitoEmail = digitoEmail[:-1]
                    tentouEmail = False
                else:
                    digitoSenha = digitoSenha[:-1]
                    senhaValida = False
                    tentouSenha = False
            elif ev.key == K_RETURN:
                if not emailValido:
                    emailValido = validarEmail(digitoEmail)
                    tentouEmail = True
                elif not senhaValida:
                    senhaValida = validarSenha(digitoSenha)
                    tentouSenha = True
                else:
                    abrirCasinha = True          
                    running = False
            else:
                if not emailValido:
                        digitoEmail += ev.unicode
                else:
                    digitoSenha += ev.unicode
                    senhaValida = False

    # Desenha na tela
    screen.fill("#97D1FA")

    draw.rect(screen, "black", rectEmail, 3)
    textoEmail = minhaFonte.render(digitoEmail, True, "#000000")
    screen.blit(textoEmail, (120, 112))

    draw.rect(screen, "black", rectSenha, 3)
    textoSenha = minhaFonte.render(digitoSenha, True, "#000000")
    screen.blit(textoSenha, (120, 212))
    if tentouEmail:
        if emailValido:
            msg = fonteValidation.render("Email válido", True, "#006400")
        else:
            msg = fonteValidation.render("Email inválido tente novamente", True, "red")
        screen.blit(msg, (100, 290))

    if tentouSenha:
        if senhaValida:
            msg = fonteValidation.render("Senha válida. Senha crptografada: " + criptografaSenha(digitoSenha), True, "#006400")
        else:
            msg = fonteValidation.render("Senha inválida tente novamente", True, "red")
        screen.blit(msg, (100, 330))

    display.update()
    clock.tick(30)

screen = display.set_mode((800, 600))
nuvem_x=500
c="#97D1FA"
running=True     
while running:
    mouseX,mouseY=mouse.get_pos()
    for ev in event.get():
        if ev.type == QUIT:
            running = False
        if ev.type == MOUSEBUTTONDOWN:
            if ev.button== 1:
                if mouseY<=200:
                    Som3.play()
#                elif mouseY<=400:
#                    Som2.play()
                else:
                    Som1.play()

    #Parte de par movimentações e simulações físicas
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

    screen.blit( minhaImagem, (500, 275))
    meuTexto= fonteCasinha.render("Superar obstáculos faz as garotas\nmais bonitas, sabia?",True, "#000000")
    screen.blit(meuTexto,(400, 150))

    display.update()

quit()
