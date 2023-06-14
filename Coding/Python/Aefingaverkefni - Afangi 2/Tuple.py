#Hreiðar Pétursson
#27.3.2023
#Æfingaverkefni fyrir tuples

# Hreiðar Pétursson
# 16janúar
# While æfingaverkefni rallý

on = True

while on == True:

    print("1. Sex stök, tvær gagnagerðir og strengir")
    print("2. Tuple með 4 lista")
    print("3. Tuple 14 stafir")
    print("4. Tuple Tölur")
    print("5. Biðja um staf og athuga hvort hann tilheyrir")
    print("6. Hætta")


    val = int(input("Hvað viltu gera?"))

    if val == 1:

        tup1 = ("strengur1","strengur2",22,23,24,25)
        print(tup1)

        #Renni afturábak í gegnum tuple listann
        #og prenta úr gildi sem er stak númer 3
        for x in range(len(tup1)-1,-1,-1):
            if x == 3:
                print("stak númer 3 er:",tup1[x])
        #Finna aftasta stakið
        for x in range(len(tup1)):
            if x == len(tup1) -1:
                print("stak sem er -1 er:",tup1[x])
        #Skrifa út öll stökin í tuple í einni línu
        for x in range(len(tup1)):
            if x == len(tup1) -1:
                print(tup1[x])
            else:
                print(tup1[x],end=":")
    elif val == 2:
        tup=([1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20])
        for x in tup:
            print(x,end=":")
        print()
        for x in range(len(tup[1])):
            if x == 1:
                print(tup[1][x])
    elif val == 3:
        tup1 = ("fjortanstafir1",2,3,4,5,6,7,8,9,10,11,12,13,14)
        for x in range(len(tup1[0])):
            if x == 4:
                print(tup1[0][x])
        for x in range(len(tup1[0])):
            if x == len(tup1[0]) -4:
                print("fjórði síðasti stafurinn er:",tup1[0][x])
        print(tup1[0][1:8])
    elif val == 4:
        tup = (1,2,3,4,5)
        tala = int(input("Sláðu inn tölu til að margfalda"))
        tup2 = []
        for x in tup:
            nyttstak = x * tala
            tup2.append(nyttstak)
        print(tuple(tup2))


    elif val == 5:
        tuple_a = ("a","v","c","x","o","y","d")
        tupa = False
        tupb = False
        tuple_b = ("b","c","e","f","r","g","h")
        stafur = input("stafur sem tilheyrir")
        for x in tuple_a:
            if x == stafur:
                tupa = True
                print("Stafurinn tilheyrir Tuple A")
        for x in tuple_b:
            if x == stafur:
                tupb = True
                print("Stafurinn tilheyrir Tuple B")

    elif val == 6:
        on = False
    else:
        print("þú hefur ekki valið rétt")

print("Takk fyrir að nota forritið mitt")