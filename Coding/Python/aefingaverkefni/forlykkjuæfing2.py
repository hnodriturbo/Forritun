#Hreiðar Pétursson
#30januar2023
#For lykkja með While
import random
on = True

while on == True:
    print("1. Summa")
    print("2. Talnabil upp niður")
    print("3. Oddatölur")
    print("4. la la la")
    print("5. margföldunartöflur")
    print("6. Linur og dálkar")
    print("7. Talnagisk")
    print("8. Hætta")

    val = int(input("Hvað viltu gera?"))

    if val == 1:
        tala1 = int(input("Sláðu inn tölu númer 1"))
        tala2 = int(input("Sláðu inn tölu númer 2"))

        summa = 0
        for x in range(tala1,tala2):
            summa = x + summa
        print(summa)

    elif val == 2:
        tala1 = int(input("Sláðu inn tölu númer 1"))
        tala2 = int(input("Sláðu inn tölu númer 2"))
        mismunur = abs(tala1-tala2)
        if tala1 > tala2 and mismunur > 1:
            for x in range(tala1,tala2,-1):
                print(x)
        else:
            for x in range(tala1,tala2):
                print(x)

    elif val == 3:
        tala1 = int(input("Sláðu inn tölu númer 1"))
        tala2 = int(input("Sláðu inn tölu númer 2"))
        for x in range(tala1,tala2):
            if x % 2 == 1:
                print(x)

    elif val == 4:
        la = int(input("hversu oft er la sungið í röð"))

        for x in range(1,la):
            print("la", end="_")


    elif val == 5:



        for tafla in range(1,11):

            for tala in range(1,11):
                summa = tafla * tala
                print(summa)


    elif val == 6:

        for x in range(1,16):
            print(x, x*2, x*3)


    elif val == 7:
        tala = random.randint(1,100)
        agiskun = int(input("giskaðu á tölu frá 1 og upp í 100"))
        print(tala)

        while agiskun != tala:
            if agiskun > tala:
                print("tala er of há")
            if agiskun < tala:
                print("tala er of lá")

            agiskun = int(input("reyndu aftur"))

            if agiskun == tala:
                print("Rétt tala")

    elif val == 8:
        on = False

print("Takk fyrir mig")