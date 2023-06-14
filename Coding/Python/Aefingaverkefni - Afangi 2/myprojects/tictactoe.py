#Hreiðar Pétursson
#8/6 2023
#tic tac toe og hangman
import random
while True:
    print("1. Tic Tac Toe")
    print("2. Hangman")
    print("3. Hætta")
    val = input("Veldu nú")
    if val == "1":
        while True:
            print("1. Spila leikinn")
            print("2. Leikreglur")
            print("3. Hætta")
            val = input("Veldu nú")
            if val == "1":
                board = [[' ', ' ', ' '],
                         [' ', ' ', ' '],
                         [' ', ' ', ' ']]
                def printboard(board):
                    for row in board:
                        print("   |   ".join(row))
                        print("-----------------")
                printboard(board)

            elif val == "2":
                pass
            elif val == "3":
                break
    elif val == "2":
        word_list = ['Python', 'Hangman', 'Computer', 'Programming', 'Challenge', 'Language', 'Keyboard', 'Solution','Algorithm', 'Victory']
        while True:
            print("1. Spila Hangman")
            print("2. Leikreglur")
            print("3. Hætta")
            val = input("Veldu nú")
            if val == "1":
                word = random.choice(word_list)
                lengd = len(word)
                giskadir_stafir = []
                #Hangman leikurinn
                print("Orðið sem valið er af tölvunni:")
                for x in word:
                    print("_",end="")
                print("")
                while True:
                    stafur = input("Sláðu inn staf til að giska á")
                    if stafur in giskadir_stafir:
                        print("Stafurinn er nú þegar búið að giska á")
                    else:
                        giskadir_stafir.append(stafur)
                    for x in word:
                        if x in giskadir_stafir:
                            print(x,end="")
                        else:
                            print("_",end="")
                    print("")
                    print("Þú ert búinn að giska á:",giskadir_stafir)
            elif val == "2":
                pass
            elif val == "3":
                break
    elif val == 3:
        break
