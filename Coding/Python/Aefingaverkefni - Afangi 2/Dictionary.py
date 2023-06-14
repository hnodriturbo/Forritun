#Hreiðar Pétursson
#Æfing Dictionary
# 22.3.2023
import math
import random

on = True
mittdict = {1:"Gulur",2:"Rauður",3:"Grænn",4:"Blár",5:"Svartur",6:"Hvítur",7:"Fjólublár",8:"Brúnn",9:"Bleikur",10:"Banani"}
while on == True:

    print("1. Búa til / Reset Dictionary")
    print("2. Prenta út Dictionary")
    print("3. Eyða lit")
    print("4. Prenta ákveðinn lit")
    print("5. Gera afrit af Dict - Eyða Dict og prenta bæði")
    print("6. Sýna notkun falla")
    print("7. Búa til nýtt Dictionary")
    print("8. Hætta")
    val = int(input("Hvað viltu gera? "))

    if val == 1:
        def mydict():
            mittdict = {1: "Gulur", 2: "Rauður", 3: "Grænn", 4: "Blár", 5: "Svartur", 6: "Hvítur",
                        7: "Fjólublár", 8: "Brúnn", 9: "Bleikur", 10: "Banani"}
            return mittdict
        print("Dictionary hefur verið búið til / Resetað")
    elif val == 2:
        print(mittdict)
    elif val == 3:
        print("Þú hefur valið að eyða lit")
        for key, value in mittdict.items():
            print("{0}:{1}".format(key,value))
        nr = int(input("Veldu hvaða lit þú vilt eyða"))
        def eydalit(nr,mittdict):
            print("Þér tókst að eyða litnum sem þú valdir sem var:",mittdict[nr])
            mittdict.pop(nr)
            return mittdict
        mittdict = eydalit(nr, mittdict)
    elif val == 4:
        for x in mittdict:
            print(x)
        nr = int(input("Veldu litinn sem þú vilt skrifa út"))
        def prentalit(nr,mittdict):
            print(mittdict[nr])
        prentalit(nr,mittdict)
    elif val == 5:
        valmynd = True
        while valmynd == True:
            print("1. Afrita Dictionary")
            print("2. Eyða Dictionary")
            print("3. Prenta út allar Dictionary")
            print("4. Hætta")
            val = int(input("Veldu nú"))
            if val == 1:
                nyttdictionary = dict(mittdict)
                nyttdictionary2 = mittdict.copy()
            elif val == 2:
                val = int(input("Veldu dictionary 1 eða 2 eða 3 til að eyða"))
                if val == 1:
                    del mittdict
                elif val == 2:
                    del nyttdictionary
                elif val == 3:
                    del nyttdictionary2
            elif val == 3:
                if 'mittdict' in locals():
                    print(mittdict)
                if 'nyttdictionary' in locals():
                    print(nyttdictionary)
                if 'nyttdictionary2' in locals():
                    print(nyttdictionary2)
            elif val == 4:
                valmynd = False
    elif val == 6:
        for key, value in mittdict.items():
            print(key,value)
        print(mittdict.keys())
        print(mittdict.values())
        print(mittdict.items())
        mittdict.clear()
    elif val == 7:
        nyttd = {}
        def nytt(nyttd):
            hversustort = int(input("Sláðu inn hversu stórt dictionary á að vera"))
            for x in range(hversustort):
                key = int(input("Sláðu inn key"))
                value = input("Sláðu inn value")
                nyttd[key] = value
            return nyttd
        print(nytt(nyttd))
    elif val == 8:
        on = False

    else:
        print("þú hefur ekki valið rétt")

print("Takk fyrir að nota forritið mitt")