# - Implemente um jogo de adivinhação. O computador "escolhe" (gera aleatoriamente) um número entre 1 e 1023, e o usuário tenta adivinhar o número escolhido (100XP);
# - Para cada tentativa do usuário, o programa deve exibir na tela (150XP):
#   - O número -1, se o número gerado for menor do que o número fornecido pelo usuário;
#   - O número 1, se o número gerado for maior do que o número fornecido pelo usuário;
#   - O número 0, se o número gerado for igual ao fornecido pelo usuário. Neste caso, o programa deve exibir o número de tentativas usadas pelo usuário para acertar a escolha do computador de finalizar a execução;
# - Implemente a variação do jogo na qual usuário e computador podem trocar de funções. O programa começa perguntando quem tentará adivinhar: o usuário ou o computador (150XP);
# - Ou seja, usuário e computador podem trocar de funções;

import random
alt=int(input("Quem vai advinhar?(1- Você\n2-Eu)"))
if alt==2:
    numSorteado=random.randint(1,1023)
    tentativas=0
    chute=0
    while chute!=numSorteado:
        chute=int(input("\nQual número você acha que eu escolhi?"))
        if chute > numSorteado:
            print("-1")
        if chute < numSorteado:
            print("1")
        tentativas+=1
    print("0\nParabéns! Acertou em %i tentativas"%tentativas)
else:
    retorno=-1
    tentativas=0
    inicio=1
    fim=1023
    print("Escolha um número entre %i e %i"%(inicio,fim))
    while retorno!=0:
        adv=random.randint(inicio,fim)
        print(adv)
        retorno=int(input("Escreva 1 caso o número seja maior\n-1 caso seja menor\n0 caso seja igual"))
        if retorno==-1:
            fim=adv+1
        if retorno==1:
            inicio=adv-1
        tentativas+=1
if retorno==0:
    print("Acertei em %i tentativas"%tentativas)
if fim<inicio:
    print("Aconteceu alguma coisa errada")
