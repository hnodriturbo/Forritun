#Hreiðar Pétursson
#30januar2023
#For lykkja með While

on = True

while on == True:
    print("1. Tölur frá 1-5")
    print("2. Jafnar tölur")
    print("3. Milli 30-40")
    print("4. Sex dálkar")
    print("5. Prenta")
    print("6. Hætta")

    val = int(input("Hvað viltu gera?"))

    if val == 1:
        for x in range(1,6):
            print(x)

    elif val == 2:
        for x in range(2,11,2):
            print(x)

    elif val == 3:
        for x in range(30,41):
            print(x)

    elif val == 4:
        teljari = 1
        for x in range(10,34):
            if teljari % 6 == 0:
                print(x)
            else:
                print(x, end=" ")
            teljari = teljari + 1
    elif val == 5:
        breyta = "A"
        for x in range(1,6):
            print(breyta)
            breyta = breyta + "A"

    elif val == 6:
        on = False

print("Takk fyrir mig")

