#Hreiðar Pétursson
#23 janúar 2023
#random æfingaverkefni
import random


while True:
    print("1. Teningakast\n"
          "2. Yatsí kast\n"
          "3. Oddatölur\n"
          "4. Break og True/false\n"
          "5. Hætta")

    val = int(input("Veldu hvað þú vilt gera"))

    if val == 1:
        # Liður 1 - Teningakast
        tala = random.randint(1,6)
        print("Random talan er",tala)

    elif val == 2:
        #Liður 2 - Yatzi kast
        teljari = 1
        summa = 0
        while teljari < 6:
            teljari = teljari + 1

            tala = random.randint(1,6)
            summa = summa + tala
            print(tala)
        print("Summa talnanna er",summa)

    elif val == 3:
        #Liður 3 - Finna oddatölur
        teljari = 0
        summa = 0

        while teljari < 25:
            teljari = teljari + 1


            tala = random.randint(0,1500)
            summa = summa + tala
            if tala % 2 == 1:
                print("ég fann oddatölu")
            else:
                print("ég fann venjulega tölu")
        print("summa talnanna er",summa)


    elif val == 4:
        #Liður 4 - break og TrueFalse
        fann99 = False
        for i in range(250):
            tala = random.randint(25,115)
            print(tala)
            if tala == 73:
                break
            if tala == 99:
                fann99 = True
        if fann99 == True:
            print("Fann töluna 99")


    elif val == 5:
        break

    else:
        print("þú hefur ekki valið rétt")
