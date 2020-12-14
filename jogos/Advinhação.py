print("************************************")
print("Seja bem vindo ao jogo de advinhação")
print("************************************")

numero_secreto = 42
tentativas = 3
rodada = 1

while (rodada <= tentativas):
    print("Tentativa {} de {}".format(rodada, tentativas))
    chute = int(input("Digite o seu numero: "))
    print("Você digitou: ", chute)

    certo = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(certo):
        print('Você acertou c:')
    else:
        if(maior):
            print('Você errou! O seu chute foi maior que o número secreto.')
        elif(menor):
            print('Você errou! O seu chute foi menor que o número secreto.')

    rodada = rodada + 1

print("Fim do Jogo")