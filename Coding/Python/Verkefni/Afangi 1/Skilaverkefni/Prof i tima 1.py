#Hreiðar Pétursson
#26 janúar 2023
#Próf í tíma
import random

on = True

while on == True:

    print("Veldu hvað þú vilt gera\n"
          "1. Aldur\n"
          "2. Reikningsdæmi\n"
          "3. Giska á tölu\n"
          "4. Hætta")

    val = int(input("Veldu hvað þú vilt gera"))

    if val == 1:
        aldur = int(input("Sláðu inn aldurinn þinn:"))

        if aldur < 0 or aldur > 110:
            print("nú ertu að ljúga")
        elif aldur < 18:
            print("Ennþá barn")
        if aldur > 17 and aldur < 110:
            print("Loksins ertu orðin fullorðinn")
        if aldur > 50 and aldur < 110:
            print("Það styttist líka í eftirlaunin þín")

    elif val == 2:
        tala1 = int(input("Sláðu inn tölu 1"))
        tala2 = int(input("Sláðu inn tölu 2"))
        tala3 = int(input("Sláðu inn tölu 3"))

        summa = tala1 + tala2

        summa2 = summa - tala3

        print("(",tala1,"+",tala2,") -",tala3,"=",summa2)


    elif val == 3:
        tala = int(input("Sláðu inn tölu á bilinu 1-15"))
        teljari = 1
        tala2 = random.randint(1,15)


        while tala != tala2:
            tala2 = random.randint(1, 15)
            print("Tölvan giskar á",tala2)
            teljari = teljari + 1

            if tala2 == tala:
                print("Tölvan giskaði á rétta tölu")
                break


        print("Tölvan giskaði",teljari,"sinnum")




    elif val == 4:
        on = False

    else:
        print("Þú hefur ekki valið rétt")

print("Takk fyrir")

