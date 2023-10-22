########## Hreiðar Pétursson ###########
  ######### Skilaverkefni 1 ##########
 ########### September 2023 ###########
import csv
from Skilaverkefni_3_klasar import *

# Gerði sér skjal til að halda utan um föllin.

# Fallið sem les CSV skránna
def lesaCSV(file, class_type):
    header = []
    instance_data = []
    try:
        with open(file, "r", newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            headerInfo = next(reader)
            header.append(headerInfo)
            for row in reader:
                if class_type == "hermannanemi":
                    instance = hermannanemi(*row)
                elif class_type == "flokkstjoranemi":
                    instance = flokkstjoranemi(*row)
                elif class_type == "foringjanemi":
                    instance = foringjanemi(*row)
                else:
                    raise ValueError("Invalid class_type")
                instance_data.append(instance)
        return header, instance_data
    except Exception as error:
        print(f"\nÞað hefur komið upp villa við að sækja gögnin úr skránni. Gripin villa :\n{error}")


# Fallið sem skrifar í CSV skránna
def skrifaCSV(file, header, instance_data):
    try:
        with open(file, "w", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(header[0])
            for instance in instance_data:
                writer.writerow(instance.to_list())
        return True
    except Exception as error:
        print(f"\nÞað kom upp villa við að skrifa gögnin í skránna. Gripin villa :\n{error}")



# Þetta prenta fall nota ég til að prenta út með __str__ (get valið hvaða klasa ég prenta úr)
def prenta(file, class_type):
    print("\nNúna ætla ég ná í gögnin úr skránni og setja hvert instance object í listann")
    header, instance_data = lesaCSV(file, class_type)
    print("\nÞað hefur tekist að ná í gögnin úr skránni")
    print("\nNúna ætla ég að prenta út hvert instance með því að nota __str__")
    for nemi in instance_data:
        print(nemi)
    print("\nAllt hefur verið prentað út. Núna skrifa ég gögnin aftur í skránna")
    success = skrifaCSV(file, header, instance_data)
    if not success:
        print("\nÞað tókst ekki að skrifa í skránna")
        return False
    else:
        print("\nAllt gekk upp og gögnin hafa verið skrifuð aftur í skránna")
        return True

# Eftir kynjum fallið   
def eftirKynjum():
    print("\nNúna ætla ég ná í gögnin úr skránni og setja hvert instance object í listann")
    header, instance_data = lesaCSV("hermannanemi.csv", "hermannanemi")
    print("\nÞað hefur tekist að ná í gögnin úr skránni")
    print("\nNúna verður prentuð út talning á kynum")
    kk_listi, kvk_listi, other_listi = hermannanemi.telja_kyn(instance_data)
    while True:
        print("\nVeldu 1 til að prenta út nöfn KK nema")
        print("Veldu 2 til að prenta út nöfn KVK nema")
        print("Veldu 3 til að prenta út alla sem flokkast sem other nema")
        print("Veldu 0 til að klára þennan lið")
        val = input("Veldu nú : ")
        while val not in ["1","2","3","0"]:
            val = input("Verður að velja 1,2,3 eða 0")
        if val == "1":
            if len(kk_listi) > 0:
                print("\nNúna verða allir KK nemar prentaðir út :")
                for kk_instance in kk_listi:
                    print(kk_instance)
            else:
                print("\nÞað eru engir KK nemendur")
        elif val == "2":
            if len(kvk_listi) > 0:
                print("\nNúna verða allir KVK nemar prentaðir út :")
                for kvk_instance in kvk_listi:
                    print(kvk_instance)
            else:
                print("\nÞað eru engir KVK nemendur")
        elif val == "3":
            if len(other_listi) > 0:
                print("\nNúna verða allir Other nemar prentaðir út :")
                for other_instance in other_listi:
                    print(other_instance)
            else:
                print("\nÞað eru engir Other nemar")
        elif val == "0":
            print("\nNúna skrifa ég gögnin í skránna aftur")
            success = skrifaCSV("hermannanemi.csv", header, instance_data)
            if success:
                print("Tókst að skrifa gögnin í skránna")
            return True

# Þrjú föll sem tengjast eftir staf. Fallið sem skilar niðurstöðunum, validation og svo það sem keyrir prógrammið   
def eftirStaf(stafur, instance_data):
    nidurstodur = []
    for hermannanemi in instance_data:
        nafn = hermannanemi.nafn
        if stafur.lower() == nafn.lower()[0]:
            nidurstodur.append(hermannanemi)
    if len(nidurstodur) > 0:
        return nidurstodur
    else:
        return False
    
def validateStafur(stafur):
    return stafur.isalpha() and len(stafur) == 1

def eftirStafProgram():
    print("\nNúna ætla ég ná í gögnin úr skránni og setja hvert instance object í listann")
    header, instance_data = lesaCSV("hermannanemi.csv", "hermannanemi")
    print("\nÞað hefur tekist að ná í gögnin úr skránni")
    
    
    while True:
        print("\nVelkominn í velja staf og fá niðurstöður prógrammið mitt")
        print("1. Stimpla inn staf")
        print("2. Hætta")
        val = input("Veldu nú")
        while val not in ["1","2"]:
            val = input("Verður að velja annaðhvort 1 eða 2")
        if val == "1":
            stafur = input("\nSláðu inn staf til að finna alla sem byrja á þeim staf : ")
            while not validateStafur(stafur):
                stafur = input("\nVerður að stimpla inn bókstaf : ")
            nidurstodur = eftirStaf(stafur, instance_data)
            if not nidurstodur:
                print("\nÞað fundust engar leitarniðurstöður")
            else:
                for index, nidurstada in enumerate(nidurstodur):
                    print(f"\nLeitarniðurstaða {index+1}:")
                    print(nidurstada)
            print("\nBúið að prenta allar leitarniðurstöður ef voru einhverjar")
        elif val == "2":
            print("\nNúna reyni ég skrifa gögnin í skránna aftur")
            success = skrifaCSV("hermannanemi.csv", header, instance_data)
            if success:
                print("Tókst að skrifa gögnin í skránna")
                return True


# Gerði þetta fall sérstaklega til að standa undir kröfum lýsingannar í verkefninu
def finnaLandherSkilaLista(instance_data):
    listiLandher = []
    
    for flokkstjoranemi in instance_data:
        herdeild = flokkstjoranemi.herdeild
        if herdeild == "Landher":
            listiLandher.append(flokkstjoranemi)
    
    return listiLandher
    
# Þetta fall er það sem keyrist frá valmyndinni         
def finnaLandher():
    # Byrja á að ná í gögnin úr skránni, gera instances og setja þau í lista
    print("\nNúna ætla ég ná í gögnin úr skránni og setja hvert instance object í listann")
    header, instance_data = lesaCSV("flokkstjoranemi.csv", "flokkstjoranemi")
    print("\nÞað hefur tekist að ná í gögnin úr skránni")
    
    # Nota hitt fallið til að ná í lista af öllum sem eru í "Landher"
    listiLandher = finnaLandherSkilaLista(instance_data)
    
    # Ef listinn hefur eitthvað innihald iterata ég í gegnum listann og prenta nafn, herdeild og símanúmer í gegnum getter
    if len(listiLandher) > 0:
        print(f"\nÞað fundust {len(listiLandher)} niðurstöður")
        
        for flokkstjoranemi in listiLandher:
            print(f"\nNafn: {flokkstjoranemi.getNafn()}")
            print(f"Herdeild: {flokkstjoranemi.getHerdeild()}")
            print(f"Sími: {flokkstjoranemi.getSimanumer()}")
        
        # Skrifa gögnin aftur í skránna (optional í rauninni)
        print("\nNúna reyni ég skrifa gögnin í skránna aftur")
        success = skrifaCSV("flokkstjoranemi.csv", header, instance_data)
        if success:
            print("Tókst að skrifa gögnin í skránna")
            return True
    # Læt fallið skila false ef það er ekkert innihald í listanum
    else:
        return False




# Tvö föll fyrir eldri en 20. Eitt sem skilar listanum og annað sem ég kalla program (útprentunin)
def eldri_20(instance_data):
    listi_eldri_20 = []
    for nemi in instance_data:
        aldur = nemi.finnaAldur()
        if aldur > 20:
            listi_eldri_20.append(nemi)
    return listi_eldri_20

def eldri_20_program():
    # Byrja á að ná í gögnin úr skránni, gera instances og setja þau í lista
    print("\nNúna ætla ég ná í gögnin úr skránni og setja hvert instance object í listann")
    header, instance_data = lesaCSV("flokkstjoranemi.csv", "flokkstjoranemi")
    print("\nÞað hefur tekist að ná í gögnin úr skránni")
        
    print("\nNúna prentast út nafn og kennitala allra sem eru eldri en 20 ára")
    
    for instance in instance_data:
        print(instance)
    
    # Sæki listann af öllum sem eru eldri en 20 með því að keyra fallið  
    listi_eldri_20 = eldri_20(instance_data)
    
    if len(listi_eldri_20) > 0:
        for nemandi in listi_eldri_20:
            print(f"\n{nemandi.getNafn()}")
            print(f"{nemandi.getKennitala()}")
        print("\nÞað tókst að prenta út alla nemendur sem eru eldri en 20")
        
    elif len(listi_eldri_20) == 0:
        print("\nÞað fundust engar niðurstöður af fólki eldra en 20 ára")
    
    else:
        return False
    
    # Skrifa gögnin aftur í skránna (optional í rauninni)
    print("\nNúna reyni ég skrifa gögnin í skránna aftur")
    success = skrifaCSV("flokkstjoranemi.csv", header, instance_data)
    if success:
        print("\nTókst að skrifa gögnin í skránna")
        return True
    else:
        print("\nTókst ekki að skrifa gögnin í skránna")
        return False  

# Tvö föll fyrir skulda herlán - annað sem skilar lista og annað fyrir keyrstu prógrams (útprentunin)  
def skuldaHerlan(instance_data):
    listiSkuldaHerlan = []
    for instance in instance_data:
        herlan = instance.getHerlan()
        
        if int(herlan) > 0:
            listiSkuldaHerlan.append(instance)
    return listiSkuldaHerlan

def skuldaHerlanProgram():
    # Byrja á að ná í gögnin úr skránni, gera instances og setja þau í lista
    print("\nNúna ætla ég ná í gögnin úr skránni og setja hvert instance object í listann")
    header, instance_data = lesaCSV("foringjanemi.csv", "foringjanemi")
    print("\nÞað hefur tekist að ná í gögnin úr skránni")
    
    listiSkuldaHerlan = skuldaHerlan(instance_data)
    
    print("\nNúna mun ég prenta út nafn og skuld allra þeirra sem skulda herlán")
    
    if len(listiSkuldaHerlan) > 0:
        for instance in listiSkuldaHerlan:
            print(f"\nNafn: {instance.getNafn()}")
            print(f"Herlán: {instance.getHerlan()}")
        print("\nÞað tókst að prenta út alla sem skulda herlán")
    elif len(listiSkuldaHerlan) == 0:
        print(f"\nÞað eru engir sem skulda herlán")
    else:
        return False
    
    # Skrifa gögnin aftur í skránna (optional í rauninni)
    print("\nNúna reyni ég skrifa gögnin í skránna aftur")
    success = skrifaCSV("foringjanemi.csv", header, instance_data)
    if success:
        print("\nTókst að skrifa gögnin í skránna")
        return True
    else:
        print("\nTókst ekki að skrifa gögnin í skránna")
        return False
    
   
# Heildarupphæð herlánsskulda - tvö föll - eitt sem skilar lista og annað fyrir keyrslu útprentunar
def heildarupphaedHerlansskulda(instance_data):
    summaHerlana = 0
    for instance in instance_data:
        herlan = instance.getHerlan()
        if int(herlan) > 0:
            summaHerlana += int(herlan)
    return summaHerlana

def heildarupphaedHerlansskuldaProgram():
    # Byrja á að ná í gögnin úr skránni, gera instances og setja þau í lista
    print("\nNúna ætla ég ná í gögnin úr skránni og setja hvert instance object í listann")
    header, instance_data = lesaCSV("foringjanemi.csv", "foringjanemi")
    print("\nÞað hefur tekist að ná í gögnin úr skránni")
    
    print("\nNúna mun ég prenta út heildarskuld allra herlána")
    
    summaHerlana = heildarupphaedHerlansskulda(instance_data)
    
    if summaHerlana > 0:
        print(f"\nSumma allra herlána er : {summaHerlana}")
    elif summaHerlana == 0:
        print(f"\nÞað skuldar engin neitt herlán")
    else:
        return False
    
    # Skrifa gögnin aftur í skránna (optional í rauninni)
    print("\nNúna reyni ég skrifa gögnin í skránna aftur")
    success = skrifaCSV("foringjanemi.csv", header, instance_data)
    if success:
        print("\nTókst að skrifa gögnin í skránna")
        return True
    else:
        print("\nTókst ekki að skrifa gögnin í skránna")
        return False
    