#Hreiðar Pétursson
#While æfing
#25 janúar 2023
on = True
while on == True:

    print("1. Liður\n"
          "2. liður\n"
          "3. liður\n"
          "4. liður\n"
          "5. hætta")

    val = int(input("Hvað viltu gera?"))

    if val == 1:

        tala = 6
        tala2 = int(input("giskaðu á tölu milli 1 og 10"))

        while tala2 != tala:
            print("Valdir vitlaust")
            tala2 = int(input("Reyndu aftur"))

            if tala2 == tala:
                print("Valdir rétt")

    elif val == 2:

       teljari = 1
       while teljari < 11:

           if teljari != 3 and teljari != 6:
                print(teljari)
           teljari = teljari + 1

    elif val == 3:
        teljari = 0
        while teljari < 11:
            print(teljari)
            teljari = teljari + 2

    elif val == 4:
        teljari = 0
        while teljari < 6:
            print("******")
            teljari = teljari + 1

    elif val == 5:
        on = False

    else:
        print("Þú hefur ekki valið rétt")