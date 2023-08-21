#Hreiðar Pétursson
#31janúar
#Strengir - Manipulation

"""
#Verkefni frá glærunum
nafn = "Anna Marín Jónasdóttir" \

stafabreyting = input("veldu hvaða staf skal breyta")

#Hérna er valda stafnum breytt í stjörnu (old,new,max)
nafn = nafn.replace(stafabreyting,"*")

print("nafnið þitt breytt",nafn)

"""

on = True

while on == True:
    print("1. Nafn")
    print("2. Að telja orð")
    print("3. Afturábak")
    print("4. Hætta")

    val = int(input("Veldu hvað þú vilt gera"))

    if val == 1:
        nafn = "Hreiðar Pétursson"
        nafn = nafn.upper()
        print(nafn)

        nafn = nafn.lower()
        print(nafn)

        nafn = nafn.replace("r","@")
        print(nafn)

    elif val == 2:
        nafn = "Hreiðar Pétursson er besti maður í öllum heiminum"

        teljari = 0

        for x in nafn:
            if x == " ":
                teljari = teljari + 1

        print("ég taldi",teljari+1,"orð í strengnum")


        teljari = 0
        for x in range(len(nafn)):
            if nafn[x] == " ":
                teljari = teljari + 1

        print(teljari+1)



    elif val == 3:
        nafn = "Hreiðar Pétursson"

        #ofugurstrengur = nafn[::-1]


        for x in range(len(nafn) -1, -1, -1):
            print(nafn[x], end="")
        print()

        #print(ofugurstrengur)

    elif val == 4:
        on = False

print("Takk fyrir að nota mig")
