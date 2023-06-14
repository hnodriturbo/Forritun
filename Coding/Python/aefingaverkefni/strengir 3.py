#Hreiðar Pétursson
#3/2/2023
#Strengja æfing 3


on = True

while on == True:

    print("1. liður")
    print("2. liður")
    print("3. hætta")


    val = int(input("Hvað viltu gera?"))

    if val == 1:
        nafn = input("vinsamlegast sláðu inn nafn")

        nafn = nafn.title()
        print(nafn)

        nafn = nafn.upper()
        print(nafn)

    elif val == 2:

        true = True
        true2 = True
        true3 = True
        strengur = ""
        bandstrik = "-"

        while true == True:
            banki = input("Sláðu inn bankanúmer")

            if len(banki) > 4:
                print("Lengd bankanúmer verður að vera 4 stafir eða minna")
                banki = input("Sláðu bankanúmer aftur")

            if len(banki) == 1:
                banki = "000" + banki
            elif len(banki) == 2:
                banki = "00" + banki
            elif len(banki) == 3:
                banki = "0" + banki

            if banki.isdigit():
                strengur = banki + bandstrik
                break
            else:
                print("banki verður að vera eingöngu tölustafir")
                banki = input("Sláðu inn bankanúmer eingöngu í tölustöfum")

        while true2 == True:

            hofudbok = input("Sláðu inn höfuðbók")

            if len(hofudbok) > 2:
                print("Lengd höfuðbókar verður að vera 2 stafir eða minna")
                hofudbok = input("Sláðu aftur inn höfuðbók")

            if len(hofudbok) == 1:
                hofudbok = "0" + hofudbok

            if hofudbok.isdigit():
                strengur = strengur + hofudbok + bandstrik
                break
            else:
                print("Höfuðbók verður að vera tölustafir")
                hofudbok = input("Sláðu höfuðbók eingöngu í tölustöfum")

        while true3 == True:

            rknnr = input("Sláðu inn reikningsnúmer")

            if len(rknnr) > 6:
                print("Lengd reikningsnúmers verður að vera 6 stafir eða minna")
                rknnr = input("Sláðu aftur inn reikningsnúmer")

            if len(rknnr) == 1:
                rknnr = "00000" + rknnr
            elif len(rknnr) == 2:
                rknnr = "0000" + rknnr
            elif len(rknnr) == 3:
                rknnr = "000" + rknnr
            elif len(rknnr) == 4:
                rknnr = "00" + rknnr
            elif len(rknnr) == 5:
                rknnr = "0" + rknnr

            if rknnr.isdigit():
                strengur = strengur + rknnr
                break
            else:
                print("Reikningsnúmer verður eingöngu að vera tölustafir")
                rknnr = input("Sláðu inn rknnr eingöngu í tölustöfum")

        print("14 stafa reikningnúmerin þín eru", strengur)



    elif val == 3:

        reikn = input("Sláðu inn reikningsnúmer")

        for x in range(0,4):
            print(reikn[x])
            if reikn[x].isdigit:
                print("tölustafir")
            else:
                print("verður að vera eingöngu tölustafir")










        #for x in list:
         #   if x.isdigit():
          #      newlist.append(x)
           # else:
            #   print("Villa")
             #   reikn = input("Reyndu aftur")










    else:
        print("þú hefur ekki valið rétt")

print("Takk fyrir að nota forritið mitt")