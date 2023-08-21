#Hreiðar Pétursson
#31janúar
#Strengir - Manipulation

on = True

strengur = input("Komdu með setningu með amk 7 orðum")

while on == True:

    print("1. bil og orð")
    print("2. fyrstu 5")
    print("3. hvað margir stafir")
    print("4. lengd")
    print("5. snúa við")
    print("6. stórir stafir")
    print("7. litlir stafir")
    print("8. hversu oft")
    print("9. @")
    print("10. Hætta")

    val = int(input("Hvað viltu gera?"))

    if val == 1:


        teljaribil = 0
        teljariord = 1

        for x in strengur:
            if x == " ":
                teljaribil = teljaribil + 1

        print("það eru",teljaribil,"bil í textanum")

        for i in strengur:
            if i == " ":
                teljariord = teljariord + 1
        print("það er",teljariord,"orð í strengnum")



    elif val == 2:


        print(strengur[:5])

    elif val == 3:

        takn = int(input("Hvað á að skrifa út marga stafi úr strengnum"))
        print(strengur[0:takn])

        for x in range(takn):
            print(strengur[x])

    elif val == 4:


        lengdstrengs = 0

        for x in strengur:
            lengdstrengs = lengdstrengs + 1

        print("lengd strengsins er",lengdstrengs)

    elif val == 5:
        stadur = 0
        stadur2 = 0

        for x in range(len(strengur)):
            if strengur[x] == " ":
                stadur = x
                break
        fyrstaord = strengur[:stadur-1]

        print(fyrstaord[::-1])

        for x in range(len(strengur)):
            if strengur[x] == " ":
                stadur2 = x
        sidastaord = strengur[stadur2+1::]

        print(sidastaord[::-1])

        midja = strengur[stadur+1:stadur2]

        print(fyrstaord[::-1],midja,sidastaord[::-1])



    elif val == 6:


        strengur = strengur.upper()

        print(strengur)

        strengur = strengur.title()

        print(strengur)
    elif val == 7:


        strengur = strengur.lower()

        print(strengur)

    elif val == 8:

        stafur = input("sláðu inn staf til að athuga hve oft hann er í strengnum")
        teljari = 0
        on = False
        for x in strengur:
            if x == stafur:
                teljari = teljari + 1
            if x == stafur:
                on = True
        if on == True:
            print("Stafurinn kom fyrir í textanum")
        elif on == False:
            print("Stafurinn kom ekki fyrir í textanum")
        print("stafurinn kom",teljari,"sinnum fyrir í textanum")

        if stafur in strengur:
            print(stafur,"kom", strengur.count(stafur),"sinnum fyrir í textanum")
        else:
            print("þessi stafur kom ekki fyrir í textanum")
    elif val == 9:

        nyrstrengur = ""

        for x in strengur:
            if x == " ":
                nyrstrengur += " "
            else:
                nyrstrengur += "@"
            #strengur = strengur.replace(x,"@")

        nyr = ""
        for x in strengur:
            if x == " ":
                nyr=nyr+x
            else:
                nyr=nyr+"@"

        print(nyrstrengur)
        print(nyr)

    elif val == 10:
        on = False
    else:
        print("þú hefur ekki valið rétt")

print("Takk fyrir að nota forritið mitt")



texti = "strengur"

for x in texti:
    #Hér er x einn stafur í einu
    print(x)

for x in range(len(texti)):
    #Hér skilar x lengd textans í tölum
    print(x) # hér er x tala
for x in range(len(texti)):
    print(texti[x]) #hér er breytan stafir

