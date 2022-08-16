'''
from tkinter import *

app = Tk()
app.title("PPT")
app.geometry("400x500")
app.resizable(0, 0)




app.mainloop()






'''
import random

print("==================================",
      "\nBem-Vindo ao Pedra, Papel e tesoura",
      "\nBy: Daniel Gomes",
      "\n==================================")

print("Selecione um elemento , você irá jogar contra um robô")
print("==================================")
print("1-Pedra","\n2-Papel","\n3-Tesoura")
print("==================================")

points_vc = 0
points_bot = 0

while True:
    points = print("Voce:", points_vc, "Bot:", points_bot)

    selecao = input("Digite aqui:")
    lista=["Pedra", "Papel", "Tesoura"]
    #t(lista)

    if selecao == "Pedra":
        bot= random.choice(lista)
        print(bot)
        escolha = bot
        if escolha == "Papel":
            print("Bot ganhou")
            points_bot += 1
        elif escolha == "Pedra":
            print("Empate")
            points_bot += 0
        elif escolha == "Tesoura":
            print("Bot perdeu")
            points_vc += 1
        
        #points_vc += 1
        #print("Voce tem:",points_vc, "PONTOS")
    elif selecao == "Papel":
        bot= random.choice(lista)
        print(bot)
        escolha = bot
        if escolha == "Papel":
            print("Empate")
            points_bot += 0
        elif escolha == "Pedra":
            print("Bot perdeu")
            points_vc += 1
        elif escolha == "Tesoura":
            print("Bot ganhou")
            points_bot += 1
    elif selecao == "Tesoura":
        bot= random.choice(lista)
        print(bot)
        escolha = bot
        if escolha == "Papel":
            print("Bot perdeu")
            points_vc += 1
        elif escolha == "Pedra":
            print("Bot ganhou")
            points_bot += 1
        elif escolha == "Tesoura":
            print("Empate")
            points_vc += 0
    else:
        print("Não entendi : (")
        


