import random 


print("************************************")
print("Seja bem vindo ao jogo de advinhação")
print("************************************")

numero_secreto = random.randrange(1, 101)
tentativas = 3


for rodada in range(1, tentativas + 1):
    print("Tentativa {} de {}".format(rodada, tentativas))
    chute = int(input("Digite um numero entre 1 e 100: "))
    print("Você digitou: ", chute)

    if (chute < 1 or chute > 100):
        print("Você deve inserir um número entre 1 e 100!")
        continue

    certo = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(certo):
        print('Você acertou c:')
        break
    else:
        if(maior):
            print('Você errou! O seu chute foi maior que o número secreto.')
        elif(menor):
            print('Você errou! O seu chute foi menor que o número secreto.')

print("Fim do Jogo")