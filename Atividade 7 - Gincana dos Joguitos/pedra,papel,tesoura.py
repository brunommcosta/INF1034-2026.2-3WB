
import random
def vitoria(p1,p2):
    if (p1=="Pedra" and p2=="Papel") or (p1=="Papel" and p2=="Tesoura") or (p1=="Tesoura"and p2=="Pedra"):
        print("Eu ganhei")
        return False
    if (p2=="Pedra" and p1=="Papel") or (p2=="Papel" and p1=="Tesoura") or (p2=="Tesoura"and p1=="Pedra"):
        print("Você ganhou!")
        return True
    if p2==p1:
        print("Empate!")


escolhas=["Pedra","Papel","Tesoura"]
decisao=""
while decisao!="n":
    jogador=str(input("O que você vai jogar?\n(Colocar letra maiúscula no início da palavra)"))
    pc=random.choice(escolhas)
    pontosJ=0
    pontosP=0
    print("Eu jogo %s\n"%pc)
    if vitoria(jogador,pc):
        pontosJ+=1
    else:
        pontosP+1
    decisao=str(input("Deseja jogar novamente? y/n"))
print("Quantidade de pontos acumulados pelo jogador: %i"%pontosJ)
print("Quantidade de pontos acumulados pelo compuador: %i"%pontosP)
