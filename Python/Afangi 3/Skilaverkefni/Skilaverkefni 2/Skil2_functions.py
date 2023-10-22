########## Hreiðar Pétursson ###########
  ######### Skilaverkefni 1 ##########
############## Ágúst 2023 ##############

import csv
import random
import Skil2_class
import Skil2_minnFlottiKlasi
# Ef klasinn væri í annarri skrá myndi ég nota þetta:
# from klasi import verkalydsfelag


# Hvert fall er ferli. Sýni skilaboð í gegnum ferlið og byggi hvert
# fall þannig að það er ysta lagið sem er prógrammið, miðju lagið sem
# er hérna í þessari skrá. Svo í sumum liðum er ég með innsta lag sem er 
# einskonar kjarni liðarins.

# Ákvað að gera fall sem býr til csv skránna
def buaTilSkra():
    nafnaListi = {
    "Gunnar Jónsson" : "1306702059",
    "Jónas Gunnarsson" : "1012862079",
    "Hannes Bjarnason" : "0507605929",
    "Gunna Gunnarsdóttir" : "0202576039",
    "Sara Karlsdóttir" : "0512871429",
    "Sigurður Ólafsson" : "1210783149",
    "Edda Jóhannsdóttir" : "2105836219",
    "Björn Sigurðarson" : "1910728470",
    "Ólöf Eiríksdóttir" : "1804597286",
    "Stefán Þórarinsson" : "0601889357"
}
    try:
        with open("verkalydsfelag.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Nr", "Nafn", "Kennitala", "Laun"])

            # Writer skrifa allt sem strengi inn í skrá
            for indexNr, (nafn, kennitala) in enumerate(nafnaListi.items()):
                laun = random.randint(300000,600000)
                writer.writerow([indexNr+1, nafn, kennitala, laun])        
        return True
    except Exception as error:
        raise error


# Þetta fall prentar út alla meðlimi úr skránni
def prentaVerkalydsfelag():
    felagsmennObjectListi = Skil2_class.medhondlaSkra.opnaSkra("verkalydsfelag.csv")
    if not felagsmennObjectListi:
        print("\nÞað kom upp einhver villa við að sækja upplýsingar úr skránni")
        return False
    else:
        print(f"\nÞað tókst að opna skránna og setja aðilana sem objects inn í lista")
        for felagsmadur in felagsmennObjectListi:
            print(felagsmadur)
        return True

def nyr_medlimur():
    # Byrja á að opna skránna og setja objectin í lista
    felagsmennObjectListi = Skil2_class.medhondlaSkra.opnaSkra("verkalydsfelag.csv")
    # Keyri prógrammið
    haedsta_nr = Skil2_minnFlottiKlasi.minnKlasi.get_haedsta_nr(felagsmennObjectListi)
    nyr_felagsmadur = Skil2_minnFlottiKlasi.minnKlasi.add_medlimur_program(haedsta_nr)
    if not nyr_felagsmadur:
        print("Eitthvað fór úrskeiðis eða hætt var við ferlið")
        return False
    else:
        print("\nÞað tókst að fá upplýsingar um nýja félagsmanninn.")
        print("\nNú reyni ég að búa til nýtt instance af félagsmanni")                
        nyr_felagsmadur_instance = Skil2_class.verkalydsfelag(*nyr_felagsmadur)
        print("\nÞað tókst að búa til instance af félagsmanni")
        felagsmennObjectListi.append(nyr_felagsmadur_instance)
        print(f"\nÞað tókst að bæta {nyr_felagsmadur_instance.nafn} í object listann")
        # Skrifa svo uppfærða object listann í skránna
        Skil2_class.medhondlaSkra.skrifaSkra(felagsmennObjectListi, "verkalydsfelag.csv")
        print("\nÞað tókst að skrifa uppfærða listann í skránna")
        return True
  
     
def eydaMedlim():
    felagsmennObjectListi = Skil2_class.medhondlaSkra.opnaSkra("verkalydsfelag.csv")
    if not felagsmennObjectListi:
        return False
    else:
        print("\nÞað tókst að búa til lista af objects úr skránni")
        valFelagsmadurObject = Skil2_minnFlottiKlasi.minnKlasi.velja_medlim_program(felagsmennObjectListi)
        if not valFelagsmadurObject:
            return False
        else:
            print("\nÞað tókst að velja félagsmann til að eyða")
            felagsmennObjectListi.remove(valFelagsmadurObject)
            print("\nÞað tókst að eyða völdum meðlim úr object listanum")
            success = Skil2_class.medhondlaSkra.skrifaSkra(felagsmennObjectListi, "verkalydsfelag.csv")
            if not success:
                print("\nÞað kom upp einhver villa við að skrifa í skránna")
            else:
                print(f"\nTókst að skrifa uppfærða listann í skránna")
                return True

# Gerði tvö breyta meðlim föll því ég var prófa þetta yield
def breytaMedlim():
    # Sýni hvað er að gerast jafnóðum - Ef það er villa þá er auðvelt að finna hvar í ferlinu hún er
    while True:
        felagsmennObjectListi = Skil2_class.medhondlaSkra.opnaSkra("verkalydsfelag.csv")
        if not felagsmennObjectListi:
            print("Ekki tókst að sækja gögnin úr skránni")
            return False
        else:
            print("\nÞað tókst að búa til lista af objects úr skránni")
            valinnFelagsmadur = Skil2_minnFlottiKlasi.minnKlasi.velja_medlim_program(felagsmennObjectListi)
            if not valinnFelagsmadur:
                print("\nEitthvað koma uppá. Líklegast var hætt við ferlið")
                return False
            else:
                print("\nÞað tókst að velja félagsmann til að breyta")
                print("\nNú verðuru send/ur í að breyta ferlið")
                success = Skil2_minnFlottiKlasi.minnKlasi.breyta_medlim_program(valinnFelagsmadur)
                if not success:
                    print("\nEitthvað kom uppá eða það var valið að hætta án breytinga")
                else:
                    print("\nBreytingarnar hafa verið staðfestar og nú verður reynt að skrifa breytingarnar í skránna")
                    success = Skil2_class.medhondlaSkra.skrifaSkra(felagsmennObjectListi, "verkalydsfelag.csv")
                    if not success:
                        print("\nÞað tókst ekki að skrifa í skránna")
                    else:
                        breytaOdrumAdila = input("\nTil hamingju! Það tókst að skrifa í skránna. Viltu breyta öðrum aðila ? || 1=Já || 2=Nei ||")
                        while breytaOdrumAdila not in ["1","2"]:
                            breytaOdrumAdila = input("Verður að velja annað hvort 1 til að breyta öðrum aðila eða 2 til að hætta")
                        if breytaOdrumAdila == "1":
                            continue
                        elif breytaOdrumAdila == "2":
                            return True
                        
def breyta_medlim():
    while True:
        felagsmennObjectListi = Skil2_class.medhondlaSkra.opnaSkra("verkalydsfelag.csv")
        if not felagsmennObjectListi:
            yield "Ekki tókst að sækja gögnin úr skránni", False
            break
        
        yield "\nÞað tókst að búa til lista af objects úr skránni\n\nNú verðuru sendur í að velja meðlim prógrammið svo þú getur valið meðlim til að breyta", True
        
        # Keyri prógrammið sem velur meðlim
        valinnFelagsmadur = Skil2_minnFlottiKlasi.minnKlasi.velja_medlim_program(felagsmennObjectListi)
        if not valinnFelagsmadur:
            yield "Eitthvað koma uppá. Líklegast var hætt við ferlið", False
            break
        # Success skilaboð
        yield "\nÞað tókst að velja félagsmann til að breyta", True
        
        # Keyri breyta meðlim prógrammið sem ég bjó til
        success = Skil2_minnFlottiKlasi.minnKlasi.breyta_medlim_program(valinnFelagsmadur)
        if not success:
            yield "Eitthvað kom uppá eða það var valið að hætta án breytinga", False
            break
        
        # Success skilaboð
        yield "\nBreytingarnar hafa verið staðfestar", True
        
        # Skrifa breytta listanum aftur í skránna
        success = Skil2_class.medhondlaSkra.skrifaSkra(felagsmennObjectListi, "verkalydsfelag.csv")
        if not success:
            yield "Það tókst ekki að skrifa í skránna", False
            break
        
        # Success skilaboð og val um að breyta öðrum aðila
        breytaOdrumAdila = input("\nTil hamingju! Það tókst að skrifa í skránna. Viltu breyta öðrum aðila ?\n|| 1=Já || 2=Nei ||")
        while breytaOdrumAdila not in ["1","2"]:
            breytaOdrumAdila = input("Verður að velja annað hvort 1 til að breyta öðrum aðila eða 2 til að hætta")
        if breytaOdrumAdila == "1":
            continue
        elif breytaOdrumAdila == "2":
            yield "\nTakk fyrir nota breyta meðlim prógrammið mitt", True
            break

# Fallið sem prentar út nafn og laun allra félagsmanna
def nafnLaun():
    felagsmennObjectListi = Skil2_class.medhondlaSkra.opnaSkra("verkalydsfelag.csv")
    if not felagsmennObjectListi:
        print("Tókst ekki að búa til lista úr skránni")
        return False
    else:
        print("\nVelkominn í Prenta út nafn og laun allra félagsmanna\n")
        for felagsmadur in felagsmennObjectListi:
            print(f"Nafn: {felagsmadur.nafn}")
            print(f"Laun: {felagsmadur.laun}\n")
    success = Skil2_class.medhondlaSkra.skrifaSkra(felagsmennObjectListi, "verkalydsfelag.csv")
    if not success:
        print("Það tókst ekki að skrifa listann í skránna")
        return False
    else:
        return True  

# Fallið sem prenta út útborguð laun allra félagsmanna
def utborgudLaun():
    felagsmennObjectListi = Skil2_class.medhondlaSkra.opnaSkra("verkalydsfelag.csv")
    if not felagsmennObjectListi:
        print("\nTókst ekki að búa til lista úr skránni")
        return False
    else:
        print("\nÞað tókst að búa til lista úr skránni")
        print("\nNúna verður prentað út útborguð laun hvers félagsmanns fyrir sig\n")
        
        for felagsmadur in felagsmennObjectListi:
            print(f"Nafn: {felagsmadur.nafn}")
            print(f"Útborguð laun: {felagsmadur.utborgud_laun()}\n")
            
        print("Núna verður reynt að skrifa listann aftur í skránna")
        
        success = Skil2_class.medhondlaSkra.skrifaSkra(felagsmennObjectListi, "verkalydsfelag.csv")
        if not success:
            print("\nÞað gekk ekki að skrifa í skránna")
        else:
            print("\nÞað tókst að skrifa í skránna")
            print("\nTakk fyrir að nota útborguð laun forritið mitt")
            return True

# Fallið sem reiknar heildarskatta allra félagsmanna   
def heildarskattar():
    felagsmennObjectListi = Skil2_class.medhondlaSkra.opnaSkra("verkalydsfelag.csv")
    if not felagsmennObjectListi:
        print("\nTókst ekki að búa til lista úr skránni")
        return False
    else:
        print("\nÞað tókst að búa til lista úr skránni")
        heildarskattur = 0
        for felagsmadur in felagsmennObjectListi:
            heildarskattur += int(felagsmadur.skatt())
            print(f"\nNafn: {felagsmadur.nafn}")
            print(f"Laun: {felagsmadur.laun}")
            print(f"Skattur: {felagsmadur.skatt():.1f}")
            print(f"Útborguð laun: {felagsmadur.utborgud_laun()}")
        print("\nNúna ætla ég að reikna heildarskatt allra félagsmanna")
        print(f"\nHeildarskattur borgaður af öllum félagsmönnum: {heildarskattur}")
        return True

    