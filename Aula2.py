print("************************************")
print("Seja bem vindo ao jogo de advinhação")
print("************************************")

numero_secreto = 42

chute = input("Digite o seu numero: ")

print("Você digitou: ", chute)

if(numero_secreto == int(chute)):
    print('Você acertou c:')
else:
    print('Você errou :c')