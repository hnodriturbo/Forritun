#Hreiðar Pétursson
#Æfing föll
# 20.3.2023
import math
import random


on = True

while on == True:
    print("1. Brandari")
    print("2. Brandarar")
    print("3. Hvers Kyns")
    print("4. Fimm tölur")
    print("5. Fimm aðgerðir")
    print("6. Reikna meðaltal")
    print("7. Finna orð")
    print("8. Rúmmál kúlu")
    print("9. Rúmmál kassa")
    print("10 Rúmmál þríhyrnings")
    print("11. Hætta")
    val = int(input("Veldu nú"))
    if val == 1:
        def brandari():
            brandari1 = "Brandari 1"
            return brandari1
    elif val == 2:
        hversumargir = int(input("Veldu á bilinu 1-3 hvaða brandara skal segja"))
        def brandarar(hversumargir):
            if hversumargir == 1:
                return "Brandari 1"
            elif hversumargir == 2:
                print("Brandari 2")
            elif hversumargir == 3:
                print("brandari 3")
            elif hversumargir not in [1,2,3]:
                print("Verður að velja 1 eða 2 eða 3")
        print(brandarar(hversumargir))
    elif val == 3:
        kyn = input("Sláðu inn kyn þitt: (kk,kvk,hvk)")
        def hverskyns(kyn="þetta kyn þekki ég ekki"):
            if kyn == "kk":
                return "Þú ert karlmaður"
            elif kyn == "kvk":
                return "Þú ert kvenmaður"
            elif kyn == "hvk":
                return "Þú ert hvorukyn"
            else:
                return kyn
        print(hverskyns())
    elif val == 4:
        listi = []
        for x in range(5):
            tala = int(input("Sláðu inn 5 tölur"))
            listi.append(tala)
        def skrifaut(listi):
            for x in range(len(listi)):
                if x == 4:
                    return listi[x]
                else:
                    print(listi[x],end=",")
        print(skrifaut(listi))
        def staersta(listi):
            staersta = max(listi)
            return staersta
        print(staersta(listi))
        def minnsta(listi):
            minnsta = min(listi)
            return minnsta
        print(minnsta(listi))
        def summa(listi):
            summa = 0
            for x in listi:
                summa = summa + x
            return summa
        print(summa(listi))
        def medaltal(listi):
            lengd = len(listi)
            summa = 0
            for x in listi:
                summa = summa + x
            medaltal = summa / lengd
            return medaltal
        print(medaltal(listi))

    elif val == 5:
        def student(breyta1="Hreiðar", breyta2="er", breyta3="bestur", breyta4="í öllum heiminum"):
            print(breyta1,breyta2,breyta3,breyta4)
        print(student("Gunnar",breyta3="langbestur",breyta4="í öllum himingeiminum!!"))
    elif val == 6:
        def reiknamedaltal(*tolur):
            summa = 0
            for x in tolur:
                summa += x
            lengd = len(tolur)
            medaltal = summa/lengd
            print("{0:.3f}".format(medaltal))

        reiknamedaltal(1,2)
        reiknamedaltal(2,3,1,4,5,6,7,7)

        def add(*b):
            result = 0
            for i in b:
                result = result + i
            return result
        print(add(1, 2, 3, 4, 5))
        print(add(10, 20))
    elif val == 7:

        def finnaord(texti,ordid):
            if ordid in texti:
                print("Orðið",ordid,"er í textanum")
            else:
                print("orðið",ordid, "er ekki í textanum")
        print(finnaord("Það er einhver hérna","blabla"))
    elif val == 8:

        def reiknarummalkulu(r):
            formula = 4.0 * math.pi * r**3
            r = formula / 3.0
            print("{0:.2f}".format(r))
        print(reiknarummalkulu(100))
    elif val == 9:
        def reiknarummalkassa(l,b,h):
            rummal = l * b * h
            return rummal
        print(reiknarummalkassa(10,5,100))
    elif val == 10:
        def flatarmalþri(b,h):
            hluti1 = b * h
            hluti2 = hluti1 / 2
            return "{0:.3f}".format(hluti2)
        print(flatarmalþri(10.59,5.36))
    elif val == 11:
        pass
    elif val == 12:
        x = input("Sláðu inn tölu 1:")
        y = input("Sláðu inn tölu 2:")
        z = input("Sláðu inn tölu 3:")
        def midja(x,y,z):
            if x > y and x < z:
                print(x, "er miðju talan")
            elif x < y and x > z:
                print(x,"er miðju talan")
            elif y > x and y < z:
                print(y, "er miðju talan")
            elif y < x and y > z:
                print(y,"er miðju talan")
            elif z < x and z > y:
                print(z,"er miðju talan")
            elif z > x and z < y:
                print(z,"er miðju talan")
        print(midja(x,y,z))
    elif val == 13:

        def fjoldihastafa():
            texti = input("Sláðu inn streng til að vita hástafi")
            teljari = 0
            for x in texti:
                if x.isupper():
                    teljari += 1
            print("það eru",teljari,"hástafir í textanum")
        print(fjoldihastafa())
    elif val == 14:
        texti = input("Sláðu inn texta til að telja tölustafina")
        def fjolditalna(texti):
            teljari = 0
            for x in texti:
                if x.isdigit():
                    teljari += 1
            print("Það eru",teljari,"tölur í textanum")
        print(fjolditalna(texti))
    elif val == 15:
        pass
    elif val == 16:
        strengur = "arnar"
        print(strengur[::-1])
    elif val == 17:
        on = False

print("Takk fyrir að nota forritið mitt !!! :)")