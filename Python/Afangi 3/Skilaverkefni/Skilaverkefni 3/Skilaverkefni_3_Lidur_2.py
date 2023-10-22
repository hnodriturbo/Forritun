########## Hreiðar Pétursson ###########
  ######### Skilaverkefni 1 ##########
 ########### September 2023 ###########

import random

try:
    while True:

        print("\n1. Tölur í öðru veldi")
        print("2. Tommur og sentimetrar")
        print("3. Nafnalisti")
        print("4. Gengur upp í 3 og 5")
        print("5. Hækka allar tölur")
        print("6. Jöfnureikningur")
        
        print("\n0. Hætta")

        val = input("Hvað viltu gera?")

        # Tölur í öðru veldi
        if val == "1":
            # Búið til lista af random tölum frá 100 til 200. Tíu tölur. 
            tolurFra100Til200 = [random.randint(100,200) for tala in range(10)]
            
            # Notið lambda og map() til að búa til nýjan lista með sömu tölum 
            # nema bara í öðruveldi.
            
            # list býr til lista, map notar lambda á hvert gildi í listanum tolurFra100Til200
            # og lambda gerir hvert x að x**2
            annadVeldi = list(map(lambda x: x**2, tolurFra100Til200))
            
            print("\nHérna er listi af tölunum sem voru random generated : ")
            print(tolurFra100Til200)
            print("\nHérna nota ég list, map og lambda til að færa tölurnar í annað veldi")
            print(annadVeldi)
        
        # Tommur og sentimetrar
        elif val == "2":
            # Búið til lista sem innheldur lengd í tommum. Tíu tölur. 
            lengdTommur = [random.randint(10,50) for tommutala in range(10)]
            
            # Notið lambda og map() til að búa til annan lista með sambærilegum 
            # lengdum í sentímetrum(1 tomma er 2.54 cm)
            lengdCm = list(map(lambda x: x*2.54, lengdTommur))
            
            # Prenta
            print("\nHérna er listi með random generated tommutölum frá 10 til 50")
            print(lengdTommur)
            print("\nHérna nota ég list map og lambda til að margfalda tommutöluna með tölunni 2.54 og fá þannig centimetra töluna")
            print(lengdCm)
            
        # Nafnalisti
        elif val == "3":
            # Búið til 10 orða nafnalista. 
            nafnalisti = ["Ólafur", "Katrín", "Björn", "Sigríður", "Jón", "Guðrún", "Einar", "Helga", "Arnar", "Elín"]

            # Notið lambda og filter til að finna öll orð sem eru 6 stafir eða lengri og setjið í annan lista
            sexStafirEdaLengra = list(filter(lambda x: len(x) >= 6, nafnalisti))
            
            print("\nHérna er listi með nöfnunum : ")
            print(nafnalisti)
            print("\nHérna eru öll nöfn sem eru með 6 stafi eða lengra nafn")
            print(sexStafirEdaLengra)

        # Gengur upp í 3 og 5
        elif val == "4":
            # Nota list comprehension til að búa til 120 tölur á bilinu 1 til 500
            tolur = [random.randint(1,500) for tala in range(120)]
            
            # Nota filter fallið til að taka inn listann og skila bara tölum sem 3 og 5 ganga upp í
            thrirOgNiu = list(filter(lambda x: x % 3 and x % 5, tolur))
            
            # Prenta
            print("\nHérna er listinn með 120 random tölum á bilinu 1 til 500 : ")
            print(sorted(tolur))
            print("\nHérna er listi þar sem ég er búinn að nota list, filter og lambda til að sía út tölurnar sem 3 og 9 ganga upp í : ")
            print(sorted(thrirOgNiu))

        # Hækka allar tölur
        elif val == "5":
            
            # Nota list comprehension til að búa til random tölu lista til að vinna með
            listi = [random.randint(50,1000) for tala in range(100)]
            
            # Nota map til að taka inn lista og bæta tölunni 21 við hverja tölu í listanum
            nyrlisti = list(map(lambda x: x + 21, listi))
            
            # Prenta
            print("\nHérna er sortaður listi af 100 random tölum frá 50 til 1000 : ")
            print(sorted(listi))
            print("\nHérna er nýr sortaður listi þar sem ég hef notað list, map og lambda til að bæta tölunni 21 við hverja tölu í fyrri listanum : ")
            print(sorted(nyrlisti))

        # Jöfnureikningur
        elif val == "6":
            # List comprehension til að búa til 10 random tölur á bilinu 1 til 10
            listi = [random.randint(1,10) for tala in range(10)]
            
            # Nota lambda og map() til að búa til nýjan lista sem reiknar út úr jöfnunni y=x*(3-x).
            jofnureikningur = list(map(lambda x: x*(3-x), listi))
            
            # Prenta listann og niðurstöðu listann af jöfnureikningnum
            print("\nHérna er listi með 10 random tölum á bilinu 1 til 10 : ")
            print(listi)
            print("\nHérna er listi þar sem er búið að reikna jöfnuna y=x*(3-x)")
            print(jofnureikningur)

        elif val == "0":
            break
        else:
            print("þú hefur ekki valið rétt")

    print("Takk fyrir að nota forritið mitt")
    
# Villu gríparinn
except Exception as error:
    print(f"Það hefur komið upp einhver villa. Gripin villa : \n{error}")