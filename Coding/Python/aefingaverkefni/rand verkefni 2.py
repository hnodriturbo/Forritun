#Hreiðar Pétursson
#23 janúar 2023
#random æfingaverkefni
import random
#Teningaspil A
while True:
    print("1. Teningaspil A\n"
          "2. Teningaspil B\n"
          "3. Teningaspil C\n"
          "4. Ágiskun A\n"
          "5. Ágiskun B\n"
          "6. hætta")

    val = int(input("Veldu hvað þú vilt gera"))

    if val == 1:
        svar = "Já"

        while svar == "Já":
            tala = random.randint(1, 6)
            print("Þú fékkst", tala)
            svar = input("Viltu kasta aftur? Já/Nei")

        if svar == "Nei":
            print("Takk fyrir að kasta")
        else:
            print("Valdir vitlaust")


    elif val == 2:

        hversuoft = int(input("hversu oft viltu rúlla teningnum?"))
        teljari = 0
        while teljari < hversuoft:
            teljari = teljari + 1
            tala = random.randint(1,6)
            print(tala)

    elif val == 3:
        teljari1 = 0
        teljari2 = 0
        teljari3 = 0
        teljari4 = 0
        teljari5 = 0
        teljari6 = 0

        hveoft = int(input("hversu oft viltu rúlla teningnum"))
        teljari = 0
        while teljari < hveoft:
            teljari = teljari + 1
            tala = random.randint(1,6)
            print(tala)
            if tala == 1:
                teljari1 = teljari1 + 1
            if tala == 2:
                teljari2 = teljari2 + 1
            if tala == 3:
                teljari3 = teljari3 + 1
            if tala == 4:
                teljari4 = teljari4 + 1
            if tala == 5:
                teljari5 = teljari5 + 1
            if tala == 6:
                teljari6 = teljari6 + 1

        print("talan 1 kom",teljari1,"sinnum")
        print("talan 2 kom",teljari2, "sinnum")
        print("talan 3 kom",teljari3, "sinnum")
        print("talan 4 kom",teljari4, "sinnum")
        print("talan 5 kom",teljari5, "sinnum")
        print("talan 6 kom",teljari6, "sinnum")


    elif val == 4:
        tala = random.randint(1, 10)
        print(tala)


        agiskun = int(input("giskaðu á tölu frá 1 uppí 10"))

        while agiskun != tala:
            if agiskun < tala:
                print("reyndu hærri tölu")

            elif agiskun > tala:
                print("reyndu lægri tölu")

            agiskun = int(input("Reyndu aftur:"))


        if agiskun == tala:
            print("þú giskaðir á rétta tölu")






    elif val == 5:
        teljari = 0
        tala = random.randint(1, 10)
        print(tala)

        agiskun = int(input("giskaðu á tölu frá 1 uppí 10"))

        while agiskun != tala:
            if agiskun < tala:
                print("reyndu hærri tölu")
                teljari = teljari + 1
            elif agiskun > tala:
                print("reyndu lægri tölu")
                teljari = teljari + 1
            agiskun = int(input("Reyndu aftur:"))

        if agiskun == tala:
            print("þú giskaðir á rétta tölu")
            print("þú giskaðir",teljari,"sinnum")



    elif val == 6:
        break
    else:
        print("Þú valdir ekki rétt")





